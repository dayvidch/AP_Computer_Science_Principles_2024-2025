import rsa as rsa

# initialize variables
key = "a"
mod_value = "b"
# if the variables are not digits, then it goes in this loop to keep ask them for the correct keys.
while key.isdigit() == False and mod_value.isdigit() == False:
    key = input("Enter the Encryption Key: " )
    mod_value = input("Enter the Modulus: " )
#once the keys are valid, it asks for a message, then it returns the encrypted message.
else:
    plaintext = input("Enter a message to encrypt: ")
    mod_value = int(mod_value)
    key = int(key)
    encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
    print("Encrypted Message:", encrypted_msg)
    