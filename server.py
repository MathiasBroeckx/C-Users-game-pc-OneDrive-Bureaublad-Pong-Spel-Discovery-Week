import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Use UDP
server_socket.bind(("127.0.0.1", 5555))  # Bind server to localhost and port
print("Server started... Waiting for players...")

players = {}  # Store player addresses and their assigned numbers
paddle_positions = {1: 150, 2: 150}  # Default paddle positions

while True:
    data, addr = server_socket.recvfrom(1024)  # Receive data from client
    message = json.loads(data.decode())  # Decode JSON message

    # Assign player number if new connection
    if addr not in players:
        if len(players) < 2:
            if len(players) == 0:
                player_number = 1
            else:
                player_number = 2
            players[addr] = player_number
            print(f"Assigned Player {player_number} to {addr}")
        else:
            print("Server full. Ignoring new connection.")
            continue  # Ignore additional players

    player_number = players[addr]  # Get assigned player number
    paddle_positions[player_number] = message["paddle_y"]  # Update paddle

    # Game state to send back
    game_state = {
        "player_number": player_number,  # Send back assigned player number
        "ball_x": 320,
        "ball_y": 240,
        "paddle1_y": paddle_positions[1],
        "paddle2_y": paddle_positions[2],
        "score": [1, 1]
    }

    # Send updated game state back to client
    server_socket.sendto(json.dumps(game_state).encode(), addr)
