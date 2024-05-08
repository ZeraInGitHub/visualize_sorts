import random
import time
import numpy as np

def visualize(a: list[int], selecting: list[int] = []) -> None:
    whattoprint = ''
    for i in range(max(a), 0, -1):
        for j in range(len(a)):
            if i <= a[j]:
                if j in selecting:
                    whattoprint += '.'
                else:
                    whattoprint += '|'
            else:
                whattoprint += ' '
        whattoprint += '\n'
    for _ in range(60 - len(a)):
        print('')
    print(whattoprint)

def shuffle(a: list[int]) -> list[int]:
    for i in range(len(a)):
        indextoswap = random.randint(0, len(a) - 1)
        a[i], a[indextoswap] = a[indextoswap], a[i]
        visualize(a, [i, indextoswap])
        time.sleep(1 / 20000)
    visualize(a)
    time.sleep(1)
    return a

def descending_shuffle(a: list[int]) -> list[int]:
    for i in range(int(np.floor(len(a) / 2))):
        a[i], a[(len(a) - 1) - i] = a[(len(a) - 1) - i], a[i]
        visualize(a, [i, (len(a) - 1) - i])
        time.sleep(1 / 100)
    visualize(a)
    time.sleep(1)
    return a

def almost_sorted(a: list[int]) -> list[int]:
    for _ in range(random.randint(3, 5)):
        first = random.randint(0, len(a)-1)
        second = random.randint(0, len(a)-1)
        while second == first:
            second = random.randint(0, len(a)-1)
        t = a[first]
        a[first] = a[second]
        a[second] = t
        visualize(a, [first, second])
        time.sleep(1 / 100)
    visualize(a)
    time.sleep(1)
    return a

def arrange(l: int) -> list[int]:
    r = []
    for i in range(l):
        r.append(i)
    return r



if __name__ == '__main__':
    visualize(arrange(4))
