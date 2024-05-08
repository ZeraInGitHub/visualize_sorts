if __name__ == '__main__':
    import visualizing
else:
    from sorting import visualizing
import time
import random


def shuffle(a: list, start_limit: int = 0) -> list:
    for _ in range(100):
        start = random.randint(start_limit, len(a) - 1)
        end = random.randint(start_limit, len(a) - 1)
        a[start], a[end] = a[end], a[start]
    return a

def bogosort(a: list) -> None:
    attempts = 0
    comparisons = 0
    not_shuffled: bool = True
    while not_shuffled:
        attempts += 1
        not_shuffled = False
        a = shuffle(a)
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                comparisons += 1
                not_shuffled = True
                break
            visualizing.visualize(a, [i, i + 1])
            print('\nAttempts:', attempts, '\nComparisons:', comparisons)
            time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nAttempts:', attempts, '\nComparisons:', comparisons)
    time.sleep(1)

def safebogosort(a: list) -> None:
    comparisons = 0
    for i in range(len(a)):
        while a[i] != i:
            comparisons += 1
            a = shuffle(a, i)
            visualizing.visualize(a, [i])
            print('\nComparisons:', comparisons)
            time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)

def stalinsort(a: list) -> None:
    comparisons = 0
    i = 1
    while i < len(a):
        if a[i] < a[i - 1]:
            a.pop(i)
            visualizing.visualize(a, [i, i - 1])
            print('\nComparisons:', comparisons)
            time.sleep(1 / 20000)
            continue
        comparisons += 1
        visualizing.visualize(a, [i, i - 1])
        print('\nComparisons:', comparisons)
        time.sleep(1 / 20000)
        i += 1
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)


def safestalinsort(a: list) -> None:
    for _ in range(5):
        i = 1
        auxiliary = []
        while i < len(a):
            while i < len(a):
                if a[i] < a[i - 1]:
                    auxiliary.append(a.pop(i))
                    visualizing.visualize(a, [i, i - 1])
                    time.sleep(1 / 20000)
                    continue
                visualizing.visualize(a, [i, i - 1])
                time.sleep(1 / 20000)
                i += 1
            a.extend(auxiliary)
            i += 1
            auxiliary = []
        for i in range(len(a)):
            auxiliary.insert(0, a[i])
            visualizing.visualize(a, [i])
            time.sleep(1 / 20000)
        for i in range(len(auxiliary)):
            a[i] = auxiliary[i]
            visualizing.visualize(a, [i])
            time.sleep(1 / 20000)
        auxiliary = []
        visualizing.visualize(a)


if __name__ == '__main__':
    safebogosort(visualizing.shuffle(visualizing.arrange(45)))