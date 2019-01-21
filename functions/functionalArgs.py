def my_func(a, b):
    # Returns 5% of the sum of a and b.
    return sum((a, b)) * 0.05


def calc(*a):
    print(a)
    return sum(a) * 0.5


print(calc(2, 4, 5, 6, 7))


def my_func_2(**kwargs):
    if 'fruit' in kwargs:
        print('My Fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


my_func_2(fruit='apple', veggie='lettuce')


def my_func_3(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


my_func_3(20, 30, 40, fruit='orange', food='eggs')
