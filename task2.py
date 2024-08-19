from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    encrypted_array = (img_array + key) % 256  

    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)

    decrypted_array = (img_array - key) % 256
    
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("Welcome to the Image Encryption/Decryption Tool!")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")
        return

    input_path = input("Enter the path to the image: ").strip()
    if not os.path.isfile(input_path):
        print("The specified image file does not exist.")
        return

    output_path = input("Enter the path where the output image will be saved: ").strip()
    key_input = input("Enter an integer key for encryption/decryption: ").strip()

    if not key_input.isdigit():
        print("Invalid key! Please enter a valid integer.")
        return

    key = int(key_input)

    if choice == 'E':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()

