def encrypt(message, key):
   encrypted_message = ""
   for char in message:
      '''
      Shifting the character's ASCII value by the key
      now I have taken the printable ascii value range from 32 to 126, total 95 ascii characters
      now at first converting the character to its ascii value by using ord(),
      then adding key to get the updated ascii value.
      but only {ord(char) + key} couldn't handle cases when the result exceeds the max range 126.
      To fix it, if it exceeds the range of 126, that time we are using modulus of 95 (as 95 ascii char in the range) and adding 32(as the range starts from 32) to wrap around the value on its printable range. before moduling, subtracting 32 to shift the ASCII value to the 0-94 range
      ex- if ascii value = 125, key = 10
      then new_char_code = 125+10 = 135, exceeds the range. exceeding amount, 135-127=8, so after wrapping new value will be 32+8 = 40
      we are also getting the same by (135-32)%95+32 = 8+32 = 40
      '''
      new_char_code = (ord(char) -32 + key) % 95 + 32
      encrypted_message += chr(new_char_code)
   return encrypted_message

def decrypt(encrypted_message, key):
   decrypted_message = ""
   for char in encrypted_message:
      '''
      similarly while decrypting if we shift the char backward by key amount
      {ord(char) - key} couldn't handle cases when the result exceeds the min range 32.
      To fix it, if it goes below the range of 32, that time we are using modulus of 95 in same way and adding 32 to the modulus result to wrap around the value on its printable range. before moduling, subtracting 32 and adding 95 shift the ASCII value to the 0-94 range so that we can perform modulation by 95
      ex- if ascii value = 40, key = 10
      then new_char_code = 40-10 = 30, violates the range. exceeding amount, 31-30=1, so after wrapping new value will be 126-1 = 125
      we are also getting the same by (40-32-10+95)%95+32 = 93%95+32 = 93+32 = 125
      '''
      new_char_code = (ord(char) - 32 - key + 95) % 95 + 32
      decrypted_message += chr(new_char_code)
   return decrypted_message

# taking user input
while True:
   message = input("Enter the message: ")
   if message == "":
      print("You have entered an empty string, enter valid strings")
   else:
      break

while True:  # i used exception handling by try-exception, so that the user enters an integer for key and put it in an infinite while loop, so that it runs until it enters an integer.
   try:
       key = int(input("Enter the key (an integer): "))
       break  # Exit the loop if input is valid
   except ValueError:
       print("Invalid input. Please enter an integer.")

mode = input("Choose mode (encrypt/decrypt): ")
mode = mode.lower()  # I converted the mode to lower so that even if anyone enters in capital letters or in mixed letters, it don't effect the job

# Performing encryption or decryption based on the chosen mode and printing the result
while True:
   if mode == "encrypt":
      encrypted_message = encrypt(message, key)
      # Print the encrypted result
      print("Encrypted message:", encrypted_message)
      break # Exit the loop if input is valid and execution was successful
   elif mode == "decrypt":
      decrypted_message = decrypt(message, key)
      # Print the encrypted result
      print("Decrypted message:", decrypted_message)
      break
   else:
      print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
      mode = input("Choose mode (encrypt/decrypt): ")
      mode = mode.lower()

# Testing
import unittest

class CipherTest(unittest.TestCase):
   # testing normal encryption
   def test_encrypt_basic(self):
      message = "hello"
      key = 3
      expected_result = "khoor"
      self.assertEqual(encrypt(message, key), expected_result)

   # testing normal decryption
   def test_encrypt_basic(self):
      message = "khoor"
      key = 3
      expected_result = "hello"
      self.assertEqual(decrypt(message, key), expected_result)
   
   # testing cases exceeding 126
   def test_encrypt_basic(self):
      message = "khoor"
      key = 478
      expected_result = "hello"
      self.assertEqual(decrypt(message, key), expected_result)
   
   # testing cases going below 32
   def test_encrypt_basic(self):
      message = "khoor"
      key = 478
      expected_result = "hello"
      self.assertEqual(decrypt(message, key), expected_result)
   

if __name__ == "__main__":
   unittest.main()