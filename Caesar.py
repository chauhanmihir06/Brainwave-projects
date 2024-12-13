def caesar_cipher(text, shift, mode):
    result = ""
    if mode not in ['encrypt', 'decrypt']:
        return "Invalid mode. Choose 'encrypt' or 'decrypt'."

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters are unchanged

    return result


# Main program
if __name__ == "__main__":
    print("Welcome to the Caesar Cipher Program!")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (e.g., 3): "))

    # Encrypt or Decrypt
    result = caesar_cipher(message, shift, mode)
    print("\nResult:")
    print(result)
