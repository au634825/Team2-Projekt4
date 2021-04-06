import os
import select
import time


def ipcRead1(ipc_fifo_name):
    timeout = time.time() + 30  # 30 seconds from now
    with open(ipc_fifo_name) as fifo:
        while True:
            data = fifo.read()
            if len(data) == 0:
                break
            print('Read: "{0}"'.format(data))
        return data


print(ipcRead1("/tmp/irradiance"))
print(ipcRead1("/tmp/voltage"))
print(ipcRead1("/tmp/current"))
print(ipcRead1("/tmp/power"))
print(ipcRead1("/tmp/temperature"))
