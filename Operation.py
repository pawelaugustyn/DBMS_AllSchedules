class Operation(object):
    def __init__(self, op, t_id, var):
        self._operation = op
        self._transactionID = t_id
        self._variableName = var

    def __str__(self):
        return self._operation + str(self._transactionID) + self._variableName

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def new(op):
        if len(op) != 3:
            raise KeyError
        try:
            insert = Operation(op[0], int(op[1]), op[2])
        except ValueError:
            exit(-1)
        return insert

    def get_operation(self):
        return self._operation

    def get_tid(self):
        return self._transactionID

    def get_var(self):
        return self._variableName

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Operation):
            return False
        return self._transactionID == other.get_tid()

    @staticmethod
    def _is_operation(operation):
        return isinstance(operation, Operation)