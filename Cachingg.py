import time
from functools import lru_cache
@lru_cache(maxsize=32)
def somework(n):
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("now running some work")
    somework(3)
    somework(6)
    somework(2)
    print("now enter number")
    input()
    somework(2)
    print("now done")

