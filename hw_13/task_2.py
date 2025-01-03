class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):

        if min_value > max_value:
            raise ValueError("Minimum value cannot be greater than maximum value.")
        if not (min_value <= current <= max_value):
            raise ValueError("Current value must be between minimum and maximum.")

        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):

        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("Maximum value cannot be less than minimum value.")
        self.max_value = max_max
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("Minimum value cannot be greater than maximum value.")
        self.min_value = min_min
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Reached maximum value")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Reached minimum value")
        self.current -= 1

    def get_current(self):
        return self.current



counter = Counter(current=7, min_value=0, max_value=10)
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()

assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()

assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут мінімум

assert counter.get_current() == 7, 'Test4'
