# calculate time
import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        duration = "{:e}".format((time.time() - start))
        print(f"{func.__name__} running {duration} seconds, result is {res}")
        return res
    return wrapper
