import celery
from proj import tasks
from random import sample

x, y = sample(range(10), 2)
a = tasks.add(x, y)
print("{} + {} = {}".format(x,y,a))

x, y = sample(range(10), 2)
b = tasks.add.apply_async((x, y),)
print("{} + {} = {}".format(x,y,b.get()))

x, y = sample(range(10), 2)
c = tasks.add.delay(x, y)
print("{} + {} = {}".format(x,y,c.get()))

x, y = sample(range(10), 2)
d = tasks.add.s(x, y)
