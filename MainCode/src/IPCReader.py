import os
import select
import struct


def encode_msg_size(size: int) -> bytes:
    return struct.pack("<I", size)


def decode_msg_size(size_bytes: bytes) -> int:
    return struct.unpack("<I", size_bytes)[0]


def create_msg(content: bytes) -> bytes:
    size = len(content)
    return encode_msg_size(size) + content


def get_message(fifo: int) -> str:
    """Get a message from the named pipe."""
    msg_size_bytes = os.read(fifo, 4)
    msg_size = decode_msg_size(msg_size_bytes)
    msg_content = os.read(fifo, msg_size).decode("utf8")
    return msg_content


def makefifo(ipc_fifo_name):
    os.mkfifo(ipc_fifo_name)


def ipcRead(ipc_fifo_name):
    try:
        # Open the pipe in non-blocking mode for reading
        fifo = os.open(ipc_fifo_name, os.O_RDONLY | os.O_NONBLOCK)
        try:
            # Create a polling object to monitor the pipe for new data
            poll = select.poll()
            poll.register(fifo, select.POLLIN)
            try:
                # Check if there's data to read. Timeout after 10 sec.
                if (fifo, select.POLLIN) in poll.poll(100000):
                    # Do something with the message
                    msg = get_message(fifo)
                    print(msg)
                else:
                    # No data, do something else
                    print("failure, no message")
            finally:
                poll.unregister(fifo)
        finally:
            os.close(fifo)
    finally:
        # Delete the named pipe when the reader terminates
        # os.remove(ipc_fifo_name)
        print("not removing")


#makefifo("/tmp/hello_ipc")
#ipcRead("/tmp/hello_ipc")
