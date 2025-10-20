import time
def bench(fn):
    def wrap(*a, **kw):
        t0 = time.perf_counter()
        out = fn(*a, **kw)
        dt = (time.perf_counter() - t0) * 1000
        return out, dt
    return wrap

