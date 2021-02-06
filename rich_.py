from rich.progress import track
import time

if __name__ == '__main__':
    for i in track(range(100)):
        print("i:{}".format(i))
        time.sleep(0.2)
