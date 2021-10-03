import time
from contextlib import contextmanager

class cm_timer_1:
 
    def __init__(self):
        pass
    
    def __enter__(self):
        self.start_time = time.time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("time:", time.time() - self.start_time, "ms")
 
@contextmanager
def cm_timer_2():
    try:
        start_time = time.time()
        yield start_time
    except OSError:
        print("We had an error!")
    finally:
        print("time:", time.time() - start_time, "ms")