def is_even(number):
    return (number & 1) == 0


assert is_even(2494563324234324234324894038**2) == True, 'Test1'
assert is_even(234234234056897**2) == False, 'Test2'
assert is_even(2433333333945638940387**3) == False, 'Test3'

