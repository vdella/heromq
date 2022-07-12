from structure import PlateQueue
from atexit import register
import zmq


def welcome():
    return 'Type <operation> <plate>\n' + \
            'Allowed operations are:\n' + \
            '> cook\n' + \
            '> eat\n' + \
            '> quit (to quit eater)\n' + \
            '> stop (to stop cooker)\n'


print(welcome())


context = zmq.Context()
print("Connecting to cooker...")
socket = context.socket(zmq.REQ)

try:
    socket.connect('tcp://localhost:5555')
except zmq.ZMQError:
    print('Could not connect to cooker.')


def close():
    socket.close()
    context.term()
    exit()


register(close)


while True:
    message = input('Type <operation> <plate>.\n')

    socket.send_string(message)
    plate_queue = socket.recv_string()
    print(plate_queue)
