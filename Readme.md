````markdown
# TCP-Chat

TCP-Chat is a simple chat application built using Python and socket programming. It allows multiple users to connect to a server and communicate with each other in real-time. The application supports nickname-based identification and adds color formatting to differentiate users.

## Features

- **Real-time communication**: Clients can send and receive messages instantly.
- **Nickname support**: Each user is identified by a unique nickname.
- **Message broadcasting**: Messages are sent to all connected clients.
- **Dynamic user management**: Handles clients joining and leaving gracefully.
- **Color-coded messages**: Assigns a unique color to each user for better readability.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or copy the project files.
2. Ensure Python 3.x is installed on your system.
3. Open a terminal and navigate to the project directory.

## Usage

### Start the Server

1. Open a terminal.
2. Run the server script:

   ```bash
   python server.py
   ```
````

3. The server will start listening for incoming connections on `127.0.0.1:1010`.

### Connect a Client

1. Open another terminal.
2. Run the client script:

   ```bash
   python client.py
   ```

3. Enter a nickname when prompted to join the chat.

### Interact

- Once connected, type a message and press Enter to send it.
- Messages from other users will appear in the terminal with their nicknames and assigned colors.

## File Structure

- **server.py**: Contains the server-side code for managing connections, broadcasting messages, and handling user disconnections.
- **client.py**: Contains the client-side code for sending and receiving messages.

## How It Works

1. **Server**:

   - Listens for incoming client connections.
   - Assigns each client a unique nickname and a color.
   - Manages broadcasting messages to all connected clients.
   - Handles client disconnections gracefully.

2. **Client**:
   - Connects to the server using a specified IP and port.
   - Sends a nickname upon connection.
   - Handles sending and receiving messages via separate threads for simultaneous operations.

## Customization

- **Host and Port**:
  Modify the `host` and `port` variables in both `server.py` and `client.py` to run the application on a different IP address or port.

- **Colors**:
  Adjust the `colors` array in `server.py` to add or modify user colors.

## Example

1. Start the server:

   ```bash
   python server.py
   ```

   Output:

   ```
   Server is listening...
   ```

2. Connect a client:

   ```bash
   python client.py
   ```

   Output:

   ```
   Please provide your nickname:
   ```

3. Start chatting:
   - Client 1: `Hello everyone!`
   - Client 2: `Hi, welcome to the chat!`

## Known Issues

- If a client disconnects unexpectedly, their session may not close immediately, potentially causing a delay in message broadcasting.

## Future Improvements

- Add support for private messaging.
- Implement a graphical user interface (GUI).
- Enhance error handling and reconnection capabilities.

---

```

```
