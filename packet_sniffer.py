import socket

def sniff():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        s.bind(("0.0.0.0", 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        print("Sniffing started... Press Ctrl+C to stop.\n")

        while True:
            data, addr = s.recvfrom(65535)
            print(f"Packet received from {addr}")

    except KeyboardInterrupt:
        print("\nSniffing stopped.")

if __name__ == "__main__":
    sniff()
