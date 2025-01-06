import os
import zipfile
import subprocess

# Prompt for keys
key1 = input("Key: ")
key2 = input("Verify key: ")

# Verify keys match
if key1 != key2:
    print("Keys do not match. Exiting.")
    exit()

print("Searching for files...")

# Scramble function for encryption/decryption
def scramble_bytes(data, key, reverse=False):
    key_ascii = [ord(char) for char in key]
    key_length = len(key_ascii)
    result = bytearray()

    for i, byte in enumerate(data):
        offset = key_ascii[i % key_length]
        result.append(byte ^ offset)  # XOR for both encryption and decryption

    return bytes(result)

# Function to decrypt a file
def drwho_decrypt(filename, key):
    print(f"Decrypting {filename}...")
    with open(filename, "rb") as f:
        data = f.read()
    unscrambled_data = scramble_bytes(data, key, reverse=True)

    output_file = "output.zip"
    with open(output_file, "wb") as f:
        f.write(unscrambled_data)
    print(f"Decrypted file saved as {output_file}.")

# Function to encrypt a file
def drwho_encrypt(filename, key):
    print(f"Encrypting {filename}...")
    with open(filename, "rb") as f:
        data = f.read()
    scrambled_data = scramble_bytes(data, key)

    output_file = "gallifrey.ohwrd"
    with open(output_file, "wb") as f:
        f.write(scrambled_data)
    print(f"Encrypted file saved as {output_file}.")

# Loop through files in the current directory
for file in os.listdir():
    if file.endswith(".py"):
        # Skip Python scripts
        continue
    elif file.endswith(".ohwrd"):
        # Begin decryption for encrypted files
        print("Beginning decryption...")
        drwho_decrypt(file, key1)
    elif file.endswith(".zip"):
        # Begin encryption for ZIP files
        print("Beginning encryption...")
        drwho_encrypt(file, key1)
    else:
        # Skip non-relevant files
        print(f"Skipping {file} (not a .zip or .ohwrd file)")

# Check if the ZIP file is valid
try:
    with zipfile.ZipFile("output.zip", "r") as zip_ref:
        zip_ref.testzip()
except zipfile.BadZipFile:
    print("You must've put the wrong password! Oops!")
    subprocess.run(["python3", ".safe.py"])

