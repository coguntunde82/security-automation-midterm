import socket


def start_server(host: str = "127.0.0.1", port: int = 9999) -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[SERVER] Listening on {host}:{port}")

        conn, addr = server_socket.accept()
        print(f"[SERVER] Connection received from {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                print("[SERVER] Client disconnected.")
                break

            message = data.decode("utf-8")
            print(f"[SERVER] Received: {message}")

            if message.lower() == "bye":
                response = "Goodbye from server"
                conn.sendall(response.encode("utf-8"))
                print("[SERVER] Closing connection.")
                break

            response = f"Server received: {message}"
            conn.sendall(response.encode("utf-8"))

        conn.close()

    except Exception as error:
        print(f"[SERVER] Error: {error}")

    finally:
        server_socket.close()
        print("[SERVER] Server shut down.")


if __name__ == "__main__":
    start_server()