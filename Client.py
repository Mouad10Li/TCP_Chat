import socket as s
import threading

host =  "127.0.0.1" 
port = 1010
client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect((host, port))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            print(message)
        except:
            print("Disconnected from the server.")
            client.close()
            break

def send_messages():
    while True:
        try:
            message = input("")
            client.send(message.encode("ascii"))
        except:
            print("You have left the chat.")
            client.close()
            break

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)
receive_thread.start()
send_thread.start()
