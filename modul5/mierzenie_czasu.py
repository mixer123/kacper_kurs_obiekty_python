from timeit import timeit, default_timer
from time import sleep

def sleeper(n):
    sleep(n)
    return n
def count_time(do_something, n):
    before = default_timer()
    do_something(n)
    after = default_timer()
    return after - before
print(count_time(sleeper, 5))
