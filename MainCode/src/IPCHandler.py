import os


def makefifo(ipc_fifo_name):
    os.mkfifo(ipc_fifo_name)


def ipcRead(ipc_fifo_name):
    with open(ipc_fifo_name) as fifo:
        while True:
            data = fifo.read()
            if len(data) == 0:
                break
            print('Read: "{0}"'.format(data))
            return data


def ipcSend(ipc_fifo_name, data):
    fifo = os.open(ipc_fifo_name, os.O_WRONLY)
    try:
        msg = f"{data}\n".encode("UTF-8")
        os.write(fifo, msg)
    except KeyboardInterrupt:
        print("\nsend to pipe done")
    finally:
        os.close(fifo)


# makefifo("/tmp/hello_ipc")
# ipcRead("/tmp/hello_ipc")
