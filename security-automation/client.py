import socket


def start_client(host: str = "127.0.0.1", port: int = 9999) -> None:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"[CLIENT] Connected to {host}:{port}")

        while True:
            message = input("Enter message for server (type 'bye' to quit): ").strip()

            if not message:
                print("[CLIENT] Please enter a message.")
                continue

            client_socket.sendall(message.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8")
            print(f"[CLIENT] Server says: {response}")

            if message.lower() == "bye":
                print("[CLIENT] Disconnecting from server.")
                break

    except ConnectionRefusedError:
        print("[CLIENT] Error: Server is not running or refused the connection.")
    except Exception as error:
        print(f"[CLIENT] Error: {error}")
    finally:
        client_socket.close()
        print("[CLIENT] Client shut down.")


if __name__ == "__main__":
    start_client()