n = 100


class Cat:
    def __init__(self):
        global n
        print("Cat init, n is", n)
        n = 50


class Dog:
    def __init__(self):
        global n
        print("Dog init, n is", n)
        n = 150


if __name__ == '__main__':
    cat = Cat()
    dog = Dog()
    print("After cat and dog are both build, the n is", n)
