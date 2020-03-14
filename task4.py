class Cached:
    def __init__(self, func):
        self.func = func
        self.cache = dict()

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        val = self.cache[args] = self.func(*args)
        return val


@Cached
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(100))
