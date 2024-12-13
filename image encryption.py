from PIL import Image
import numpy as np


def encrypt_image(input_path, output_path, key):
    """Encrypts an image by adding a key to pixel values."""
    image = Image.open(input_path)
    image_array = np.array(image)

    # Encrypt: Add the key modulo 256 (to stay within byte range)
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved at {output_path}")


def decrypt_image(input_path, output_path, key):
    """Decrypts an image by subtracting the key from pixel values."""
    image = Image.open(input_path)
    image_array = np.array(image)

    # Decrypt: Subtract the key modulo 256
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved at {output_path}")


def main():
    print("Image Encryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1/2): ")

    input_path = input("Enter the path of the input image: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()
    key = int(input("Enter the encryption key (integer): "))

    if choice == '1':
        encrypt_image(input_path, output_path, key)
    elif choice == '2':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice! Please enter 1 for encryption or 2 for decryption.")


if __name__ == "__main__":
    main()
