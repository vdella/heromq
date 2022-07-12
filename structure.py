from prettytable import PrettyTable


class PlateQueue:

    plates = dict()
    size = 3

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
        else:
            print('Desired plate was **{}**.'.format(plate))

    def remove(self, plate):
        if not self.empty() and self.plates.get(plate) > 0:
            self.plates[plate] -= 1
        else:
            print('Desired plate was **{}**.'.format(plate))

    def __len__(self):
        length = 0

        for key in self.plates.keys():
            length += self.plates[key]

        return length

    def full(self):
        status = self.size - len(self) == 0

        if status:
            print('Full queue. Eat food.')

        return status

    def empty(self):
        status = len(self) == 0

        if status:
            print('Empty queue. Cook food.')

        return status


if __name__ == '__main__':
    queue1 = PlateQueue()

    for _ in range(10):
        print(queue1.empty())
        queue1.add('Spaghetti')
