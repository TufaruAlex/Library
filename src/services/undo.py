class UndoException(Exception):
    pass


class Undo:
    def __init__(self):
        self.__history = []
        self.__index = -1

    def undo(self):
        if self.__index < 0:
            raise UndoException("There's no operation to undo")
        self.__history[self.__index].undo()
        self.__index -= 1

    def redo(self):
        self.__index += 1
        if self.__index >= len(self.__history):
            raise UndoException("There's no operation to redo")
        self.__history[self.__index].redo()

    def record(self, operation):
        self.__history.append(operation)
        self.__index += 1


class Operation:
    def __init__(self, undo_function, redo_function=None):
        self.__undo_function = undo_function
        self.__redo_function = redo_function

    def undo(self):
        self.__undo_function.call_function()

    def redo(self):
        if self.__redo_function is None:
            pass
        else:
            self.__redo_function.call_function()


class CascadingOperation:
    def __init__(self, operations):
        self.__operations = operations

    def undo(self):
        for operation in self.__operations:
            operation.undo()

    def redo(self):
        for operation in self.__operations:
            operation.redo()


class CallFunction:
    def __init__(self, function_name, *function_parameters):
        self.__function_name = function_name
        self.__function_parameters = function_parameters

    def call_function(self):
        self.__function_name(*self.__function_parameters)
