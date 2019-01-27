from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
sammy = Dog(age=2, breed='german sh', name='tommy')
print(sammy)
print(sammy.name)  # 'tommy'

