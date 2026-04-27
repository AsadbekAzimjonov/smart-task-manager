import time


def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Task took {end_time - start_time} seconds")
        return result
    return wrapper