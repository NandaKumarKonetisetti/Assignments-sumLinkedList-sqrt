import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrapper
    
    
@timer
def calculate_sum(li):
    return sum(li)
    
val = list(map(int,input("Enter numbers to calculate its sum ").split()))
print(calculate_sum(val))
