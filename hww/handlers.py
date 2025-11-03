def handle_client(conn, addr, buffer_size, morelogic, logicinput):
    print(f"Connected by {addr}")
    conn.sendall(b"Hi there!\n")

    try:
        while True:
            data = conn.recv(buffer_size)
            if not data:
                print("Client disconnected.")
                break
            print("Received:", data.decode())
            # Pass conn and addr to your logic
            morelogic(logicinput, conn, addr, data)
    except Exception as e:
        print("Error:", e)
