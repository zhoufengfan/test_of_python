import threading
import time

print("Some string in thread2_.py")


class Action(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # name is a attr to show for identifying a thread when there is some error occurred in a single thread.
        # self.name="work"
        # If one hasn't specified the name, the name of the Thread will be Thread-i(i is 1,2,3,4,5,6,...)
        print("{} thread has inited".format(self.name))

    def run(self):
        print("Thread {} start".format(self.name))
        self.foo(self.name)
        print("Thread {} finish".format(self.name))

    def foo(self, thread_name):
        for i in range(5):
            time.sleep(0.2)
            print(thread_name)


if __name__ == '__main__':
    thread1 = Action()
    thread2 = Action()

    thread1.start()
    thread2.start()
    # thread1.join()
    # thread2.join()
