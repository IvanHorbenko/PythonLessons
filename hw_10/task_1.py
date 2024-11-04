def pow(x):
    return x ** 2

def some_gen(begin, end, func):

    current = begin
    for i in range(end):
        yield current
        current = func(current)

gen = some_gen(2, 4, pow)
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
