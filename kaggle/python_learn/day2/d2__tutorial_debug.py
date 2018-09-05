def f(n):
    return n * 2

x = 12.5

print(type(x), type(f), sep='\n')

print(x)
print(f)


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(f, 1),
    squared_call(f, 1),
    sep='\n'
)