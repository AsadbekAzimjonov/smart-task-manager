import time


def track_time(func):
    def wrapper(*args, **kwargs):
        # 1. Start the clock
        start_time = time.time()

        # 2. Call the function and store its result
        result = func(*args, **kwargs)

        # 3. Stop the clock
        end_time = time.time()
        # 4. Print "Task took X seconds"
        print(f"Task took {end_time - start_time} seconds")
        # 5. Return the result
        return result
        pass

    return wrapper