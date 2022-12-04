#Know how long a function took to execute

import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value
    return wrapper

@timed
def timing_function(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


timing_function(580)