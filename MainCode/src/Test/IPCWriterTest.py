import os
import struct


def encode_msg_size(size: int) -> bytes:
    print(type(struct.pack("<I", size)))
    return struct.pack("<I", size)


def create_msg(content: bytes) -> bytes:
    size = len(content)
    return encode_msg_size(size) + content


if __name__ == "__main__":
    IPC_FIFO_NAME = "/tmp/hello_ipc"

    fifo = os.open(IPC_FIFO_NAME, os.O_WRONLY)
    try:
        while True:
            name = input("Enter a name: ")
            content = f"{name}".encode("utf8")
            msg = create_msg(content)
            print(content)

            os.write(fifo, content)
    except KeyboardInterrupt:
        print("\nGoodbye!")
    finally:
        os.close(fifo)
