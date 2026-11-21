# === Stage 61: Add performance timing for core list and search operations ===
# Project: MealPrepBox
import time

def time_operation(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    print(f"[{elapsed*1000:.2f} ms] {func.__name__}({args}, {kwargs})")
    return result

class PerformanceTracker:
    def __init__(self):
        self.ops = []

    def __call__(self, func, *args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        self.ops.append((func.__name__, args, kwargs, elapsed))
        print(f"[{elapsed*1000:.2f} ms] {func.__name__}({args}, {kwargs})")
        return result

    def summary(self):
        for name, args, kwargs, elapsed in self.ops:
            print(f"{name}: {elapsed*1000:.2f} ms")
        return self.ops
