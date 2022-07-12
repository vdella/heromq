from patterns.singleton import Singleton
from prettytable import PrettyTable


class PlateQueue(metaclass=Singleton):

    plates = dict()
    size = 20

    def __str__(self):
        table = PrettyTable()
        table.field_names = ['Plate', 'Units']

        for name, qtt in self.plates.items():
            table.add_row([name, qtt])

        return str(table)

    def add(self, plate):
        if not self.plates.get(plate):
            self.plates[plate] = 0

        if not self.full():
            self.plates[plate] += 1

    def remove(self, plate):
        if not self.empty() and self.plates.get(plate) > 0:
            self.plates[plate] -= 1

    def full(self):
        status = self.size - len(self.plates.values()) == 0

        if status:
            print('Full queue. Eat food.')

        return status

    def empty(self):
        status = len(self.plates.values()) == 0

        if status:
            print('Empty queue. Cook food.')

        return status


if __name__ == '__main__':
    queue1 = PlateQueue()
    queue2 = PlateQueue()
    queue1.add('Spaghetti')
    print(queue2)
