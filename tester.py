import celery
from proj import tasks
from random import sample

x, y = sample(range(10), 2)
a = tasks.add(1,2)
print("{} + {} = {}".format(x,y,a))

x, y = sample(range(10), 2)
b = tasks.add.apply_async((3,4),)
print("{} + {} = {}".format(x,y,b.get()))

x, y = sample(range(10), 2)
c = tasks.add.delay(5,6)
print("{} + {} = {}".format(x,y,c.get()))

x, y = sample(range(10), 2)
d = tasks.add.s(7,8)
print("{} + {} = {}".format(x,y,d()))
