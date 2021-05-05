import threading
import time

print("Some string in thread2_")


class Action(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Thread {} start".format(self.name))
        self.foo(self.name)
        print("Thread {} finish".format(self.name))

    def foo(self, thread_name):
        for i in range(5):
            time.sleep(0.2)
            print(thread_name)


if __name__ == '__main__':
    thread1 = Action("work")
    thread2 = Action("rest")

    thread1.start()
    thread2.start()
    # thread1.join()
    # thread2.join()
