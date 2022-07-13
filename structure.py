from prettytable import PrettyTable
from multiprocessing import Lock


class PlateQueue:

    plates = dict()
    size = 3

    def __init__(self):
        self.lock = Lock()

    def __str__(self):
        table = PrettyTable()
        table.field_names = ['Plate', 'Units']

        for name, qtt in self.plates.items():
            table.add_row([name, qtt])

        return str(table)

    def add(self, plate):
        self.lock.acquire()
        if not self.plates.get(plate):
            self.plates[plate] = 0
        self.lock.release()

        self.lock.acquire()
        if not self.full():
            self.plates[plate] += 1
        self.lock.release()

    def remove(self, plate):
        self.lock.acquire()
        if not self.empty() and self.plates.get(plate) > 0:
            self.plates[plate] -= 1
        self.lock.release()

    def __len__(self):
        length = 0

        for key in self.plates.keys():
            length += self.plates[key]

        return length

    def full(self):
        return len(self) == self.size

    def empty(self):
        return len(self) == 0


if __name__ == '__main__':
    queue1 = PlateQueue()

    for _ in range(10):
        print(queue1.empty())
        queue1.add('Spaghetti')
