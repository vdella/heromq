from structure import PlateQueue
import zmq


def cook(food: str):
    PlateQueue().add(food)


def connect():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    return socket, context


while True:
    cooker, ctx = connect()
    print('Connected!')
    msg = cooker.recv_string()

    if msg == 'stop':
        cooker.close()
        ctx.term()
        exit()

    cook(msg)
