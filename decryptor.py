import os
from cryptography.fernet import Fernet

# This part load the encryption key 

with open("key.txt", "rb") as key_file:
    key = key_file.read()
# Initialize the Fernet object with the key allowing decryption
fernet = Fernet(key)
target_folder = "test_data"

# Loop through all encrypted files in the target folder and decrypt them

for file_name in os.listdir(target_folder):
    if file_name.endswith(".encrypted"):

# Joins the folder name and the file name to get the full path
        file_path = os.path.join(target_folder, file_name)
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
# Restore the original file name by removing the ".encrypted" extension
        original_name = file_name.replace(".encrypted", "")
        with open(os.path.join(target_folder, original_name), "wb") as f:
            f.write(decrypted_data)
# Remove the encrypted file after decryption
        os.remove(file_path)

print("[+] Files decrypted successfully.")
