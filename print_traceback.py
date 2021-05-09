import traceback


def foo1():
    print("foo1")
    foo2()


def foo2():
    print("foo2")
    raise RuntimeError("ops")


if __name__ == '__main__':
    try:
        foo1()
    except Exception:
        print(traceback.format_exc())
