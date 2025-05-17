def caesar_cipher():
    # Ask the user what they want to do
    action = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()

    if action not in ['E', 'D']:
        print("Invalid choice! Please type 'E' for Encrypt or 'D' for Decrypt.")
        return

    try:
        shift = int(input("Enter the shift key (a positive integer): "))
    except ValueError:
        print("Invalid input! Shift key must be a number.")
        return

    message = input("Enter the message: ")

    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if action == 'E':
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep non-letters (spaces, punctuation) as-is

    print("\nResult:")
    print(result)

# Make sure to call the function so it runs
caesar_cipher()
