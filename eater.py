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
    """Denotes operations to be done during program exiting.
    Closes ao sockets and terminates their unified context."""
    [connection.close() for connection in sockets]
    context.term()


register(close)


def generate(i):
    """Randomly gets an operation and a type of plate for
    initializing communication with the cooker. connect()s
    to a socket and sends its operation and plate-type
    for stating if it must be cooked or if it will be eaten."""
    operation = 'cook' if randint(0, 100) < 50 else 'eat'
    plate = 'Cookie' if randint(0, 100) < 50 else 'Cake'

    connect()

    sockets[i].send_string('{} {}'.format(operation, plate))
    plate_queue = sockets[i].recv_string()
    print(plate_queue)


if __name__ == '__main__':
    for _ in range(10):  # Creates 10 processes.
        process = Process(target=generate, args=(0,))
        process.start()
        process.join()
