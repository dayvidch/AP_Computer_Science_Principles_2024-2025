#   a212_rsa_decrypt.py
import rsa as rsa

# key = int(input("Enter the Decryption Key: " ))
# mod_value = int(input("Enter the Modulus: " ))
# encrypted_msg = input("What message would you like to decrypt (No brackets): ")

# #break apart the list that is cut/copied over on ", "
# msg = encrypted_msg.split(", ")
# print (rsa.decrypt(key,mod_value , msg))


# initialize variables
key = "a"
mod_value = "b"
# if the variables are not digits, then it goes in this loop to keep ask them for the correct keys.
while key.isdigit() == False and mod_value.isdigit() == False:
    key = input("Enter the Decryption Key: " )
    mod_value = input("Enter the Modulus: " )
#once the keys are valid, it asks for a message, then it returns the decrypted message.
else:
    encrypted_msg = input("What message would you like to decrypt (No brackets): ")
    msg = encrypted_msg.split(", ")
    print (rsa.decrypt(key,mod_value , msg))

