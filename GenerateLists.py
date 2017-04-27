from Schedule import Schedule


class GenerateLists(object):
    def __init__(self, transactions):
        self._transactions = transactions
        self._transCounter = []
        self._list = []
        self._counter = 0
        for i in range(0, len(self._transactions)):
            self._transCounter.append(0)

    def counter(self):
        return self._counter

    def generate_lists(self):
        bottom = True
        for i in range(0, len(self._transactions)):
            if self._transCounter[i] < len(self._transactions[i]):
                self._list.append(self._transactions[i][self._transCounter[i]])
                self._transCounter[i] += 1
                self.generate_lists()
                self._transCounter[i] -= 1
                self._list.pop()
                bottom = False
        if bottom:
            # print(self._list)
            sch = Schedule(self._list)
            if sch.is_conflict_serializable():
                self._counter += 1
                print(sch.get_printable_schedule())
