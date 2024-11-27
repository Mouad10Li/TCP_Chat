import socket as s
import threading

host = "127.0.0.1" #you can use your private ip address or public ip address if you want your server to be on the internet 
port = 1010
server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind((host, port))
server.listen()

nicknames = []
clients = []

colors = [
    "\033[91m",  
    "\033[92m",  
    "\033[93m",  
    "\033[94m", 
    "\033[95m",  
    "\033[96m", 
]
default_color = "\033[0m"  
nickname_colors = {}

def broadcast_messages(message):
    """Send a message to all connected clients."""
    for client in clients:
        try:
            client.send(message.encode("ascii"))
        except:
            remove_client(client)

def remove_client(client_socket):
    """Handle a disconnected client."""
    if client_socket in clients:
        index = clients.index(client_socket)
        clients.remove(client_socket)
        client_socket.close()
        nickname = nicknames.pop(index)
        nickname_colors.pop(nickname, None)
        broadcast_messages(f"{nickname} left the chat!")
        print(f"{nickname} left the chat.")

def handle_client(client_socket):
    """Handle an individual client."""
    try:
        
        nickname = client_socket.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client_socket)

        color = colors[len(nicknames) % len(colors)]
        nickname_colors[nickname] = color

        print(f"{nickname} joined the chat!")
        broadcast_messages(f"{nickname} joined the chat!")

        while True:
            
            message = client_socket.recv(1024).decode("ascii")
            color = nickname_colors[nickname]
            formatted_message = f"{color}{nickname}: {message}{default_color}"
            broadcast_messages(formatted_message)
    except:
        remove_client(client_socket)

def connection():
    print("Server is listening...")
    while True:
        client_socket, address = server.accept()
        print(f"Connection established with {address}.")
        client_socket.send("Please provide your nickname: ".encode("ascii"))
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

connection()
