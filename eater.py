from multiprocessing import Process
from random import randint
from atexit import register
import zmq


context = zmq.Context()
sockets = list()


def connect():
    socket = context.socket(zmq.REQ)

    try:
        socket.connect('tcp://localhost:5555')
        print('Connected.')
        sockets.append(socket)
    except zmq.ZMQError:
        print('Could not connect to cooker.')


def close():
    [connection.close() for connection in sockets]
    context.term()


register(close)


def generate(i):
    operation = 'cook' if randint(0, 100) < 50 else 'eat'
    plate = 'Cookie' if randint(0, 100) < 50 else 'Cake'

    connect()

    sockets[i].send_string('{} {}'.format(operation, plate))
    plate_queue = sockets[i].recv_string()
    print(plate_queue)


if __name__ == '__main__':
    for _ in range(10):
        process = Process(target=generate, args=(0,))
        process.start()
        process.join()
