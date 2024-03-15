'''

def encrypt_data(data, key):
    """
    Encrypts provided data using the specified key.

    Parameters:
    data (str): The data to be encrypted.
    key (str): The encryption key to use for encrypting the data.

    Returns:
    str: The encrypted data.
    """
    # Example implementation
    # This is a placeholder. You'd replace this with your encryption logic,
    # possibly using an existing encryption library for the actual work.
    encrypted_data = data  # Placeholder for actual encryption logic
    return encrypted_data

    #suggestion
    i looked around and found many people using crypto so maybe we can implement it
    to make it work you need to istall pycryptodome




def decrypt_data(encrypted_data, key):
# Write potential solution


'''
import os  # Importing the OS module for file operations
from Crypto.Cipher import AES  # Importing AES cipher from the Crypto library
from Crypto.Util.Padding import pad, unpad  # Importing padding functions from Crypto library
import base64  # Importing base64 encoding/decoding functionality

def encrypt_data(data, key):
    """
    Encrypts provided data using the specified key.

    Parameters:
    data (bytes): The data to be encrypted.
    key (bytes): The encryption key to use for encrypting the data.

    Returns:
    bytes: The encrypted data.
    """
    # Creating an AES cipher object with the specified key and selecting CBC mode
    cipher = AES.new(key, AES.MODE_CBC)
    # Encrypting the data with padding to ensure it's a multiple of the block size
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    # Encoding the initialization vector (IV) and ciphertext in base64
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    # Returning the IV concatenated with the ciphertext
    return iv.encode('utf-8') + ct_bytes

def decrypt_data(encrypted_data, key):
    """
    Decrypts provided data using the specified key.

    Parameters:
    encrypted_data (bytes): The data to be decrypted.
    key (bytes): The encryption key to use for decrypting the data.

    Returns:
    bytes: The decrypted data.
    """
    # Extracting the IV and ciphertext from the encrypted data
    iv = encrypted_data[:16]
    ct = encrypted_data[16:]
    # Creating an AES cipher object with the specified key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypting the ciphertext and removing padding
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    # Returning the decrypted plaintext
    return pt

def encrypt_file(file_path, key):
    # Opening the file in binary read mode
    with open(file_path, "rb") as f:
        # Reading the plaintext data from the file
        plaintext = f.read()
    # Encrypting the plaintext data using the encrypt_data function
    encrypted_data = encrypt_data(plaintext, key)
    # Writing the encrypted data to a new file with ".enc" extension
    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    # Opening the encrypted file in binary read mode
    with open(file_path, "rb") as f:
        # Reading the encrypted data from the file
        encrypted_data = f.read()
    # Decrypting the encrypted data using the decrypt_data function
    decrypted_data = decrypt_data(encrypted_data, key)
    # Removing the ".enc" extension from the file name
    decrypted_file_path = os.path.splitext(file_path)[0]
    # Writing the decrypted data to a new file
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_data)
