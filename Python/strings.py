string = "IEOFIT#1"

bin_string = ""
for count,char in enumerate(string):
    ascii_val = ord(char) # Gets ascii value in base 10
    bin_val = bin(ord(char)).lstrip('0b').rjust(8,'0') # bin() - Gets binary format, lstrip('0b') - strips the string '0b', rjust(8,'0') - string must contain at least 8 char as missing space will be replaced with 0
    bin_string += bin_val + " " # Format will be XXXXXXXX YYYYYYYY

    print(f"char[{count}] - {char} - {ascii_val} - {bin_val}")

print(f"\nBinary string: {bin_string}")

bin_string = bin_string.replace(" ", "") # Eliminates empty spaces
bin_string_len = str(len(bin_string)).rjust(9)

print(f"Length: {bin_string_len}")

left = bin_string[:32]
right = bin_string[32:64]

'''
String is 32 bits in length:
1st iteration - 0 to 8 -> string join with a whitespace ' '
2nd iteration - 8 to 16 -> string join with a whitespace ' ' and so forth
'''
formatted_display = ' '.join(left[i : i + 8] for i in range(0, len(left), 8))

print(f"\nLeft: {formatted_display.rjust(44)}") 

formatted_display = ""
formatted_display += ' '.join(right[i: i + 8] for i in range(0, len(right), 8))

print(f"Right: {formatted_display.rjust(43)}")