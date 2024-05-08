if __name__ == '__main__':
    import visualizing
else:
    from sorting import visualizing
import time
import math


def convert_base(n: int, b: int = 10) -> str:
    result = []
    while n > 0:
        result.insert(0, n % b)
        n = n // b
    return str(result)

def write_auxiliary(a: list, auxiliary: list, start_index: int = 0, time_division: int = 20000) -> list:
    for i in range(start_index, len(auxiliary) + start_index):
        a[i] = auxiliary[i - start_index]
        visualizing.visualize(a, [i])
        time.sleep(1 / time_division)
    return a

def quicksort(a: list[int]) -> None:
    if len(a) <= 1:
        return None
    pivot = a[len(a) - 1]
    lessthanpivot = []
    greaterthanpivot = []
    i = 0
    j = 0
    k = 0
    while i < len(a) - 1:
        i += 1
        if a[i] <= pivot:
            j += 1
            if i > j:
                a[i], a[j] = a[j], a[i]
        visualizing.visualize(a, [i, j])
        time.sleep(0.0001)
    while k < j:
        lessthanpivot.append(a[k])
        k += 1
    k += 1
    while k <= i:
        greaterthanpivot.append(a[k])
        k += 1
    quicksort(lessthanpivot)
    quicksort(greaterthanpivot)
    a = lessthanpivot
    a.append(pivot)
    a.extend(greaterthanpivot)
    visualizing.visualize(a)

def beginnermergesort(a: list) -> None:
    if math.log2(len(a)) % 1 > 1:
        print('BEGINNER MERGE SORT error: length of the list is not a power of 2')
        time.sleep(1)
        return None
    for i in range(int(math.log2(len(a)))):
        for j in range(int(len(a) // (2 ** (i + 1)))):
            for k in range(i + 1):
                if a[k + (j * (2 ** (i + 1)))] > a[k + (2 ** (i + 1)) + (j * (2 ** (i + 1)))]:
                    a[k + (j * (2 ** (i + 1)))], a[k + (2 ** (i + 1)) + (j * (2 ** (i + 1)))] = a[k + (2 ** (i + 1)) + (j * (2 ** (i + 1)))], a[k + (j * (2 ** (i + 1)))]
                visualizing.visualize(a, [k + (j * (2 ** (i + 1))), k + (2 ** (i + 1)) + (j * (2 ** (i + 1)))])
    
def firstlastsort(a: list) -> None:
    if len(a) <= 1:
        return None
    i = 0
    j = len(a) - 1
    pivot = 0
    pivot_index = 0
    k = 0
    less = []
    greater = []
    while i < j:
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
        visualizing.visualize(a, [i, j])
        time.sleep(1 / 100)
    if i == j:
        pivot = i
        pivot_index = a[pivot]
    while k < i:
        less.append(a[k])
        k += 1
    while k == pivot:
        k += 1
    while k < len(a):
        greater.append(a[k])
        k += 1
    firstlastsort(less)
    firstlastsort(greater)
    result = less
    if pivot != 0:
        result.append(pivot_index)
    result.extend(greater)
    visualizing.visualize(result)

def splittingsort(a: list) -> None:
    a = splitoddandeven(a)
    for i in range(int(len(a) / 2)):
        if a[i * 2] > a[(i * 2) + 1]:
            a[i * 2], a[(i * 2) + 1] = a[(i * 2) + 1], a[i * 2]
        visualizing.visualize(a, [i * 2, (i * 2) + 1])
        time.sleep(1 / 20000)
    a = splitoddandeven(a)

def splitoddandeven(a: list) -> list:
    auxiliary = []
    for i in a:
        if i % 2 == 0:
            auxiliary.append(i)
        visualizing.visualize(a, [i])
        time.sleep(1 / 20000)
    write_auxiliary(a, auxiliary)
    auxiliary = []
    return a

def radixsortbase4(a: list) -> None:
    for i in range(len(convert_base(max(a), 4))):
        auxiliary = []
        bucket1 = []
        bucket2 = []
        bucket3 = []
        bucket4 = []
        for j in range(len(a)):
            if a[j] // (i + 1) % 4 == 0:
                bucket1.append(a[j])
            if a[j] // (i + 1) % 4 == 1:
                bucket2.append(a[j])
            if a[j] // (i + 1) % 4 == 2:
                bucket3.append(a[j])
            if a[j] // (i + 1) % 4 == 3:
                bucket4.append(a[j])
            visualizing.visualize(a, [j])
            time.sleep(1 / 200)
        auxiliary = bucket1
        auxiliary.extend(bucket2)
        auxiliary.extend(bucket3)
        auxiliary.extend(bucket4)
        write_auxiliary(a, auxiliary, time_division=200)

if __name__ == '__main__':
    beginnermergesort(visualizing.shuffle(visualizing.arrange(32)))