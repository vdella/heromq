from prettytable import PrettyTable
from multiprocessing import Lock


class PlateQueue:

    plates = dict()
    size = 3

    def __init__(self):
        self.lock = Lock()

    def __str__(self):
        """Overrides __str__() default implementation to
        be more user-friendly, as results will be shown in a PrettyTable()."""
        table = PrettyTable()
        table.field_names = ['Plate', 'Units']

        for name, qtt in self.plates.items():
            table.add_row([name, qtt])

        return str(table)

    def add(self, plate):
        self.lock.acquire()
        if not self.plates.get(plate):
            self.plates[plate] = 0  # Initializes plate if not found.
        self.lock.release()

        self.lock.acquire()
        if not self.full():
            self.plates[plate] += 1
        self.lock.release()

    def remove(self, plate):
        self.lock.acquire()
        if self.plates.get(plate) and self.plates[plate] > 0:  # Checks key existence and if its value is > 0.
            self.plates[plate] -= 1
        self.lock.release()

    def __len__(self):
        """Overrides __len__() default implementation to ease size checking for
        self. :returns: the number of plates ready to be eaten in the queue."""
        length = 0

        for key in self.plates.keys():
            length += self.plates[key]

        return length

    def full(self):
        return len(self) == self.size
