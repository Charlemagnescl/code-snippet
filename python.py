
"""
Timer decorator for functions
"""
import time
def time_it(func):
    def inner(*args,**kwargs):
        start = time.time()
        re = func(*args,**kwargs)
        end = time.time()
        print('Time cost of function{name}: {time}sec'.format(time=end-start, name=func.__name__))
        return re
    return inner
    
"""
Python multiprocessing
"""
from multiprocessing import Pool, Lock, Process, Manager

# callback function, which would be call when the child process run into error.
def error_callback(e):
    print(e)

def multiprocessing():
    p = Pool(processes=4)
    
    # use manager.list to create list that could be shared among processes.
    manager = Manager()
    _list = manager.list()
    
    for i in range(4):
        p.apply_async(func=run, args=(_list,),error_callback=error_callback)
    
    # must invoke close() before join.
    p.close()
    p.join()
