from os import system, getcwd

from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Hash import HMAC, SHA256
from Crypto.Signature import pss

class Security: # Superclass.
    def __init__(self):
        # Location of various key files.
        self.base_key_path = getcwd() + "\\KeyFile\\"
        self.client_public_key = self.base_key_path + "client_public.pem"
        self.client_private_key = self.base_key_path + "client_private.pem"
        self.server_public_key = self.base_key_path + "server_public.pem"
        self.default_encoding = 'utf-8'
        
    # Get key from file and return it in binary format.
    def get_key_from_file(self, key_file):
        key = RSA.import_key(open(key_file, "rb").read())
        return key

    # Plaintext has to be encoded first.
    # Public key in binary format.
    def rsa_encrypt(self, plaintext, public_key):
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext

    # Ciphertext has to be encoded first.
    # Private key in binary format.
    def rsa_decrypt(self, ciphertext, private_key):
        cipher = PKCS1_OAEP.new(private_key)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext

    # Plaintext have to be encoded first.
    def aes_encrypt(self, plaintext):
        session_key = get_random_bytes(32)
        cipher = AES.new(session_key, AES.MODE_CBC)
        
        padded_data = pad(plaintext, AES.block_size)
        ciphertext_bytes = cipher.encrypt(padded_data)

        iv = cipher.iv
        
        # After b64 encoding iv, iv will be constant length of 24 bytes.
        b64encoded_iv = b64encode(iv).decode(self.default_encoding)

        b64encoded_ciphertext = b64encode(ciphertext_bytes).decode(self.default_encoding)

        # Combine both iv and ciphertext to become one string.
        b64encoded_iv_and_ciphertext = b64encoded_iv + b64encoded_ciphertext

        return b64encode(session_key).decode(self.default_encoding), b64encoded_iv_and_ciphertext

    # iv - b64 encoded. 
    # iv_and_ciphertext - b64 encoded.
    def aes_decrypt(self, key, iv_and_ciphertext):
        # First 24 bytes will be iv.
        iv = b64decode(iv_and_ciphertext[0:24])

        # After the initial 24 bytes, it will be the ciphertext.
        ciphertext = b64decode(iv_and_ciphertext[24:])

        key = b64decode(key)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(padded_plaintext, AES.block_size)

        return plaintext.decode(self.default_encoding)

    # message - has to be encoded first.
    # secret_key - binary format.
    def get_hmac(self, message, secret_key):
        new_hmac = HMAC.new(secret_key, digestmod=SHA256)
        new_hmac.update(message)

        # Returns hex representation instead of bytes.
        return new_hmac.hexdigest()

    # message - has to be encoded first.
    # secret_key - binary format.
    # mac - hex representation or hexdigest.
    def verify_hmac(self, message, secret_key, mac):
        new_hmac = HMAC.new(secret_key, digestmod=SHA256)
        new_hmac.update(message)

        try:
            new_hmac.hexverify(mac)
            return True

        except ValueError:
            return False

    # private_key - binary format.
    # returns b64 encoded signature.
    def rsa_sign(self, message, private_key):
        digest = SHA256.new(message)
        signature = pss.new(private_key).sign(digest)

        return b64encode(signature).decode(self.default_encoding)
    
    # signature - binary format.
    # public_key - binary format
    def rsa_verify(self, message, signature, public_key):
        digest = SHA256.new(message)
        verifier = pss.new(public_key)

        try:
            verifier.verify(digest, signature)
            return True
        
        except (ValueError, TypeError):
            return False

    # Data must be in binary format.
    def get_file_hash(self, data):
        hash_sha256 = SHA256.new()
        hash_sha256.update(data)

        return hash_sha256.hexdigest()

    def generate_encrypted_data(self, data):
        b64_encoded_session_key, b64_encoded_iv_and_ciphertext = self.aes_encrypt(data.encode(self.default_encoding))

        rsa_signature_b64_encoded_iv_and_ciphertext = self.get_rsa_signature(b64decode(b64_encoded_iv_and_ciphertext))
        
        server_pub_key = self.get_key_from_file(self.server_public_key)
        b64_encoded_rsa_encrypted_session_key = b64encode(self.rsa_encrypt(b64decode(b64_encoded_session_key), server_pub_key)).decode(self.default_encoding)
        
        # [344 Bytes RSA signature] [344 Bytes RSA encrypted session key] [X Bytes IV and Ciphertext]
        encrypted_data = rsa_signature_b64_encoded_iv_and_ciphertext + b64_encoded_rsa_encrypted_session_key + b64_encoded_iv_and_ciphertext
        return encrypted_data

    def decrypt_received_data(self, encrypted_data):
        # [344 Bytes RSA signature] [344 Bytes RSA encrypted session key] [X Bytes IV and Ciphertext]
        rsa_signature_b64_encoded_iv_and_ciphertext = encrypted_data[0:344]
        b64_encoded_rsa_encrypted_session_key = encrypted_data[344:688]
        b64_encoded_iv_and_ciphertext = encrypted_data[688:]

        verified = self.verify_rsa_signature(rsa_signature_b64_encoded_iv_and_ciphertext, b64_encoded_iv_and_ciphertext)

        if verified:
            client_priv_key = self.get_key_from_file(self.client_private_key)
            b64_encoded_session_key = b64encode(self.rsa_decrypt(b64decode(b64_encoded_rsa_encrypted_session_key), client_priv_key))
            
            plaintext = self.aes_decrypt(b64_encoded_session_key, b64_encoded_iv_and_ciphertext)
            return plaintext
        
        else:
            return None    

    # 344 Bytes - signature
    def get_rsa_signature(self, data):
        client_priv_key = self.get_key_from_file(self.client_private_key)
        rsa_signature_b64_encoded_iv_and_ciphertext = self.rsa_sign(data, client_priv_key)
       
        return rsa_signature_b64_encoded_iv_and_ciphertext

    def verify_rsa_signature(self, signature, data):
        server_pub_key = self.get_key_from_file(self.server_public_key)
        verification_results = self.rsa_verify(b64decode(data), b64decode(signature), server_pub_key)

        return verification_results