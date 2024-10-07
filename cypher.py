# Caesar Cipher Algorithm

def encrypt(text, shift):
    encrypted_text = ""
    
    # Traverse the message
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char  # Non-alphabetical characters remain unchanged
            
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    
    # Traverse the message
    for char in text:
        # Decrypt uppercase characters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char  # Non-alphabetical characters remain unchanged
            
    return decrypted_text

# User Input
def caesar_cipher():
    choice = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt: ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'encrypt':
        print(f"Encrypted Message: {encrypt(message, shift)}")
    elif choice == 'decrypt':
        print(f"Decrypted Message: {decrypt(message, shift)}")
    else:
        print("Invalid choice! Please select 'encrypt' or 'decrypt'.")

# Run the program
if __name__ == "__main__":
    caesar_cipher()
