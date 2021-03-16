import os
import struct


def create_msg(content: bytes) -> bytes:
    size = len(content)
    # return encode_msg_size(size) + content
    return content


def ipcSend(ipc_fifo_name, data):
    fifo = os.open(ipc_fifo_name, os.O_WRONLY)
    try:
        content = f"{data}\n".encode("UTF-8")
        msg = create_msg(content)
        os.write(fifo, msg)
    except KeyboardInterrupt:
        print("\nGoodbye!")
    finally:
        os.close(fifo)


def encode_msg_size(size: int) -> bytes:
    return struct.pack("<I", size)


def decode_msg_size(size_bytes: bytes) -> int:
    return struct.unpack("<I", size_bytes)[0]

# ipcSend("/tmp/resistance", "0")
