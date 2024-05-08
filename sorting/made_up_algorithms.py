if __name__ == '__main__':
    import visualizing
else:
    from sorting import visualizing
import time

def greatersort(a: list) -> None:
    comparisons = 0
    swaps = 0
    for _ in range(len(a)):
        end = len(a)
        start = 1
        for _ in range(len(a) - 1):
            index = start
            while a[index] < a[start - 1]:
                comparisons += 1
                index += 1
                if index >= end:
                    break
                comparisons += 1
                visualizing.visualize(a, [start, end, index])
                print('\nComparsions:', comparisons, '\nSwaps:', swaps)
                time.sleep(1 / 20000)
            if index >= end:
                while start > 0 and end > 0:
                    comparisons += 1
                    start -= 1
                    end -= 1
                    a[start], a[end] = a[end], a[start]
                    swaps += 1
                    visualizing.visualize(a, [start, end, index])
                    print('\nComparsions:', comparisons, '\nSwaps:', swaps)
                    time.sleep(1 / 20000)
                if end <= 0:
                    comparisons += 1
                    break
            else:
                a[start], a[index] = a[index], a[start]
                swaps += 1
            start += 1
            visualizing.visualize(a, [start, end, index])
            print('\nComparsions:', comparisons, '\nSwaps:', swaps)
            time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nComparsions:', comparisons, '\nSwaps:', swaps)
    time.sleep(1)

def multiplysort(a: list) -> None:
    for i in range(len(a)):
        for j in range(len(a)):
            if a[(j * (i + 1)) % len(a)] > a[(j * (i + 2)) % len(a)]:
                a[(j * (i + 1)) % len(a)], a[(j * (i + 2)) % len(a)] = a[(j * (i + 2)) % len(a)], a[(j * (i + 1)) % len(a)]
            visualizing.visualize(a, [(j * (i + 1)) % len(a), (j * (i + 2)) % len(a)])
            time.sleep(1 / 20000)


if __name__ == '__main__':
    multiplysort(visualizing.shuffle(visualizing.arrange(50)))