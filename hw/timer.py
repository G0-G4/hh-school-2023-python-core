import time

def time_it(func):
    def inner(*args, **kwargs): 
        print(func, 'started')
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(func, 'duration :', end - start)
        return res
    return inner
