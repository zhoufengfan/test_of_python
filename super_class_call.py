class Animal:
    def __init__(self):
        print("some str in class Animal")


class Dog(Animal):
    def __init__(self):
        # super().__init__()
        print("some str in class Dog")


if __name__ == '__main__':
    dog = Dog()
