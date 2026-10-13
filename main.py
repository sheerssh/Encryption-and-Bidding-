alphabet = "abcdefghijklmnopqrstuvwxyz"

text = input("Enter your message: ")
shift = int(input("Enter shift: "))

result = ""

for char in text:
    if char.lower() in alphabet:
        index = alphabet.index(char.lower())
        new_index = (index + shift) % 26

        new_char = alphabet[new_index]

        if char.isupper():
            new_char = new_char.upper()

        result += new_char
    else:
        result += char

print("Encrypted message:", result)