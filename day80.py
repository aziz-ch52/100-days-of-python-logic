# Program: Caesar Cipher (Encryption and Decryption)

# Step 1: Define function for Caesar Cipher
def caesar_cipher(text, shift, mode):
    """
    Encrypts or Decrypts text using Caesar Cipher

    Parameters:
        text (str): Input message
        shift (int): Shift value
        mode (str): 'encrypt' or 'decrypt'
    """

    # Step 2: Initialize result string
    result = ""

    # Step 3: Normalize shift within 0-25
    shift = shift % 26

    # Step 4: Traverse each character
    for char in text:

        # Check if character is alphabet
        if char.isalpha():

            # Determine ASCII base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')

            # Apply shift based on mode
            if mode == "encrypt":
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:  # decrypt
                new_char = chr((ord(char) - base - shift) % 26 + base)

            result += new_char

        else:
            # Keep non-alphabet characters unchanged
            result += char

    # Step 5: Return result
    return result


# Step 6: Take input from user
text = input("Enter text: ")
shift = int(input("Enter shift value: "))
mode = input("Enter mode (encrypt/decrypt): ").lower()

# Step 7: Validate mode
if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode.")
else:
    output = caesar_cipher(text, shift, mode)
    print("Result:", output)

# End of Program
