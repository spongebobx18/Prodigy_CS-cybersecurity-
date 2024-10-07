from PIL import Image
import numpy as np

# Function to encrypt an image by modifying pixel values
def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    img_array = np.array(img)
    
    # Encrypt: Apply a simple pixel value transformation
    encrypted_array = (img_array + key) % 256  # Shift pixel values by the key and ensure values are within 0-255 range
    
    # Save the encrypted image
    encrypted_img = Image.fromarray(np.uint8(encrypted_array))
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

# Function to decrypt an image by reversing the pixel value changes
def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    img = Image.open(input_image_path)
    img_array = np.array(img)
    
    # Decrypt: Reverse the pixel value transformation
    decrypted_array = (img_array - key) % 256  # Reverse the shift using the same key
    
    # Save the decrypted image
    decrypted_img = Image.fromarray(np.uint8(decrypted_array))
    decrypted_img.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

# Main function to run encryption/decryption
def image_encryption_tool():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    input_image = input("Enter the input image path: ")
    output_image = input("Enter the output image path: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if choice == 'encrypt':
        encrypt_image(input_image, output_image, key)
    elif choice == 'decrypt':
        decrypt_image(input_image, output_image, key)
    else:
        print("Invalid choice! Please select 'encrypt' or 'decrypt'.")

# Run the program
if __name__ == "__main__":
    image_encryption_tool()
