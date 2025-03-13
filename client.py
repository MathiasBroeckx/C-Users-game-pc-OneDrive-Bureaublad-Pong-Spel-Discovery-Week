import socket
import json
import time
import random  # Simulate paddle movement

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Use UDP
server_address = ("127.0.0.1", 5555)

player_number = None  # To store assigned player number

while True:
    paddle_y = random.randint(100, 300)  # Simulating paddle movement

    # Send paddle position to server
    message = {"paddle_y": paddle_y}
    client_socket.sendto(json.dumps(message).encode(), server_address)

    # Receive game state
    data, _ = client_socket.recvfrom(1024)
    game_state = json.loads(data.decode())

    # Store player number if first time receiving it
    if player_number is None:
        player_number = game_state["player_number"]
        print(f"You are Player {player_number}")

    print("Updated Game State:", game_state)

    time.sleep(0.1)  # Small delay to simulate real-time updates (10 FPS)
