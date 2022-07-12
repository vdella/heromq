from structure import PlateQueue
from atexit import register
import zmq


plate_queue = PlateQueue()


def cook(food: str):
    plate_queue.add(food)


def eat(food):
    plate_queue.remove(food)


context = zmq.Context()
socket = context.socket(zmq.REP)
try:
    socket.bind('tcp://*:5555')
except zmq.ZMQError:
    print('Socket already in use.')


def close():
    socket.close()
    context.term()
    exit()


register(close)


while True:
    print('Waiting.')
    message = socket.recv_string()
    operation, plate = message.split()

    if operation == 'cook':
        cook(plate)
    elif operation == 'eat':
        eat(plate)

    print(plate_queue)
    socket.send_string(str(plate_queue))
