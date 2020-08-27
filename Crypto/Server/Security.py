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
        self.server_public_key = self.base_key_path + "server_public.pem"
        self.server_private_key = self.base_key_path + "server_private.pem"
        self.client_public_key = self.base_key_path + "client_public.pem"
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

    # key - b64 encoded.
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

    # message - has to be encoded first.
    # private_key - binary format.
    # returns b64 encoded signature.
    def rsa_sign(self, message, private_key):
        digest = SHA256.new(message)
        signature = pss.new(private_key).sign(digest)

        return b64encode(signature).decode(self.default_encoding)
    
    # message - has to be encoded first.
    # signature - binary format.
    # public_key - binary format
    def rsa_verify(self, message, signature, public_key):
        digest = SHA256.new(message)
        verifier = pss.new(public_key)

        try:
            verifier.verify(digest, signature)
            return True # Verified.
        
        except (ValueError, TypeError):
            return False # Not verified.

    # Data must be in binary format.
    def get_file_hash(self, data):
        hash_sha256 = SHA256.new()
        hash_sha256.update(data)

        return hash_sha256.hexdigest()