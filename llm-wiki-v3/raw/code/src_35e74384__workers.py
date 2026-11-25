import time

def chore(args):
    name, seconds, t0 = args
    start = time.perf_counter() - t0
    time.sleep(seconds)  # waiting, not computing
    return name, start, time.perf_counter() - t0  # measured INSIDE the task


def cpu_heavy(n):
    total = 0
    for i in range(n):
        total += i
    return total