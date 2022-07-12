from structure import PlateQueue
import zmq


def eat(food):
    PlateQueue().remove(food)


def connect():
    context = zmq.Context()
    print("Connecting to cooker...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    return socket, context


def welcome():
    return 'Type <operation> <plate>\n' + \
            'Allowed operations are:\n' + \
            '> cook\n' + \
            '> eat\n'


print(welcome())

while True:
    eater, ctx = connect()
    command = input('Type <operation> <plate>.\n')
    operation, plate = command.split()

    match operation:
        case 'cook':
            eater.send_string(plate)
        case 'stop':
            eater.send_string(operation)
        case 'eat':
            eat(plate)
        case 'help':
            print(welcome())
        case 'quit':
            eater.close()
            ctx.term()
            exit()
        case _:
            print('Unknown command!')

    print(PlateQueue())
