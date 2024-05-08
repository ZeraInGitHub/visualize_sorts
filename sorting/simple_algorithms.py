if __name__ == '__main__':
    import visualizing
else:
    from sorting import visualizing
import time

def bubblesort(a: list[int]) -> None:
    comparisons = 0
    for i in range(len(a) - 1):
        for j in range((len(a) - 1) - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            comparisons += 1
            visualizing.visualize(a, [len(a) - i, j, j + 1])
            print('\nComparisons:', comparisons)
            time.sleep(0.0006)
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)

def insertionsort(a: list) -> None:
    comparisons = 0
    for i in range(len(a) - 1):
        j = i + 1
        while a[j - 1] > a[j] and j != 0:
            comparisons += 1
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
            visualizing.visualize(a, [i, j, j - 1])
            print('\nComparisons:', comparisons)
            time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)

def selectionsort(a: list) -> None:
    comparisons = 0
    for i in range(len(a) - 1):
        selecting = i
        for j in range(i, len(a)):
            if a[j] < a[selecting]:
                selecting = j
            comparisons += 1
            visualizing.visualize(a, [i, j, selecting])
            print('\nComparisons:', comparisons)
            time.sleep(1 / 20000)
        a[i], a[selecting] = a[selecting], a[i]
        visualizing.visualize(a)
        print('\nComparisons:', comparisons)
        time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)
    
def oddevensort(a: list) -> None:
    comparisons = 0
    for i in range(len(a)):
        j = i % 2
        while j < len(a) - 1:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            comparisons += 1
            j += 2
            visualizing.visualize(a, [j, j + 1])
            print('\nComparisons:', comparisons)
            time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)

def betterselectionsort(a: list) -> None:
    comparisons = 0
    for i in range(len(a)):
        for j in range(len(a) - i):
            if a[i + j] < a[i]:
                a[i], a[i + j] = a[i + j], a[i]
            comparisons += 1
            visualizing.visualize(a, [i, i + j])
            print('\nComparisons:', comparisons)
            time.sleep(1 / 20000)
        visualizing.visualize(a, [i])
        print('\nComparisons:', comparisons)
        time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)

def doublebetterselectionsort(a: list) -> None:
    comparisons = 0
    for i in range(len(a)):
        for j in range(len(a) - (2 * i)):
            if a[i + j] < a[i]:
                a[i], a[i + j] = a[i + j], a[i]
            comparisons += 1
            if a[i + j] > a[(len(a) - i) - 1]:
                a[(len(a) - i) - 1], a[i + j] = a[i + j], a[(len(a) - i) - 1]
            comparisons += 1
            visualizing.visualize(a, [i, i + j, (len(a) - i) - 1])
            print('\nComparisons:', comparisons)
            time.sleep(1 / 20000)
        visualizing.visualize(a, [i])
        print('\nComparisons:', comparisons)
        time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)

def combsort(a: list) -> None:
    comparisons = 0
    for i in range(len(a) - 1):
        for j in range(1 + i):
            if a[j] > a[j + ((len(a) - 1) - i)]:
                a[j], a[j + ((len(a) - 1) - i)] = a[j + ((len(a) - 1) - i)], a[j]
            comparisons += 1
            visualizing.visualize(a, [j, j + ((len(a) - 1) - i)])
            print('\nComparisons:', comparisons)
            time.sleep(1 / 20000)
    visualizing.visualize(a)
    print('\nComparisons:', comparisons)
    time.sleep(1)

if __name__ == '__main__':
    ...
