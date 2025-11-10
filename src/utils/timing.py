# src/utils/timing.py

import time

def bench(fn):
    def wrap(*a, **kw):
        t0 = time.perf_counter()
        out = fn(*a, **kw)
        dt = (time.perf_counter() - t0) * 1000.0  # ms
        return out, dt
    return wrap

def ms_now():
    return time.perf_counter() * 1000.0


