import os
import select
import struct
import time


def makefifo(ipc_fifo_name):
    os.mkfifo(ipc_fifo_name)


def get_message(fifo: int) -> str:
    """Get a message from the named pipe."""
    msg_size_bytes = os.read(fifo, 4)
    msg_size = decode_msg_size(msg_size_bytes)
    msg_content = os.read(fifo, msg_size).decode("utf8")
    return msg_content


def encode_msg_size(size: int) -> bytes:
    return struct.pack("<I", size)


def decode_msg_size(size_bytes: bytes) -> int:
    return struct.unpack("<I", size_bytes)[0]


def ipcRead1(ipc_fifo_name):
    timeout = time.time() + 30  # 30 seconds from now
    with open(ipc_fifo_name) as fifo:
        while True:
            data = fifo.read()
            if len(data) == 0:
                break
            print('Read: "{0}"'.format(data))
            return data


def ipcRead(ipc_fifo_name):
    fifo = os.open(ipc_fifo_name, os.O_RDONLY | os.O_NONBLOCK)
    try:
        # Create a polling object to monitor the pipe for new data
        poll = select.poll()
        poll.register(fifo, select.POLLIN)
        try:
            # Check if there's data to read. Timeout after 1 sec.
            if (fifo, select.POLLIN) in poll.poll(5000):
                # Do something with the message
                msg = os.read(fifo, 15).decode("utf8")
            else:
                # No data, do something else
                msg = -2
        finally:
            poll.unregister(fifo)
    finally:
        os.close(fifo)
        return msg


def ipcSend(ipc_fifo_name, data):
    fifo = os.open(ipc_fifo_name, os.O_WRONLY)
    try:
        msg = str(data).encode("utf-8")
        os.write(fifo, msg)
    except KeyboardInterrupt:
        print("\nsend to pipe done")
    finally:
        os.close(fifo)

# makefifo("/tmp/hello_ipc")
# ipcSend("/tmp/hello_ipc", "fewf")
# print(ipcRead("/tmp/hello_ipc"))
