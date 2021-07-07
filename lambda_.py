x = lambda a: a * 2
y = lambda a, b: a + b
z = lambda a, b: (1, 3), 5

if __name__ == '__main__':
    print("x(50) is", x(50))
    print("y(1,2) is", y(1, 2))
    # print("type(z(1, 2)) is", type(z(1, 2)))
    print("z[0],z[1](52) is", z[0]("foo", "bar"), z[1])

    l = [1, 2, 1, 8, 2]
    l0 = list(filter(lambda a: a % 2 == 0, l))
    print("l0 is", l0)
