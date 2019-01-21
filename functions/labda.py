def my_func(a):
    return a ** 2


my_nums = [1, 2, 3, 4, 5]

for item in map(lambda num: num ** 2, my_nums):
    print(item)

print(list(map(my_func, my_nums)))


def check_event(num):
    return num % 2 == 0


print(list(filter(check_event, my_nums)))
