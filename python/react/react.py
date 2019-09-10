class InputCell(object):
    def __init__(self, initial_value):
        self._value = initial_value
        self._callbacks = []
        self.is_evaluating = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if self._value != v:
            self._value = v
            for cb in self._callbacks:
                cb(v)

    def add_callback(self, fn):
        self._callbacks.append(fn)


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self._callbacks = []
        self._inputs = inputs
        for cell in self._inputs:
            cell.add_callback(self.on_change)
        self.compute_function = compute_function
        self._value = self.compute()
        self._should_eval = False

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        try:
            self._callbacks.remove(callback)
        except ValueError:
            pass

    def compute(self):
        inputs_values = [input_cell.value for input_cell in self._inputs]
        return self.compute_function(list(inputs_values))

    @property
    def is_evaluating(self):
        return self.compute() != self._value

    def on_change(self, v):
        is_evaluating = any(map(lambda i: i.is_evaluating, self._inputs))
        if is_evaluating:
            return
        new_value = self.compute()
        if new_value != self._value:
            self._value = new_value
            for cb in self._callbacks:
                cb(self._value)

    @property
    def value(self):
        return self._value

