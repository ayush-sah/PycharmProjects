# Generate an infinite sequence using generator

def gen():
    a = 0
    while True:
        yield a
        a += 1

num = gen()
while True:
    print(next(num))