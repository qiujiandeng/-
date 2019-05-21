def f1():
    print("f1被调用")

def f2():
    print("f2被调用")

def fx(fn):
    print(fn)
    fn()

fx(f1)