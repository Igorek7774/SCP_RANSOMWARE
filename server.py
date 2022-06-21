import socket

IP_ADDRESS = 'my ip address'
PORT = 5678

print("Creating Socket")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Listening for connectinions...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established!')
    with conn:
        while True:
            host_and_key = conn.recv(102)
            with open('encrypted_host.txt', 'a') as f:
                f.write(host_and_key.decode()+'\n')
            break
        print('Connection completed and closed!')

