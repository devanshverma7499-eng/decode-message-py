message = input("Enter your message: ")

encoded = ""

for char in message:
    encoded += chr(ord(char) + 3)

print("Secret Message:", encoded)

decoded = ""

for char in encoded:
    decoded += chr(ord(char) - 3)

print("Original Message:", decoded)