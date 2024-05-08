if __name__ == '__main__' or __name__ == 'simple_algorithms':
    import visualizing
else:
    from sorting import visualizing
import time

def split_odd_and_even(a: list) -> list:
    auxiliary = []
    for i in a:
        if i % 2 == 0:
            auxiliary.append(i)
        visualizing.visualize(a, [i])
        time.sleep(1 / 20000)
    for i in range(len(auxiliary)):
        j = 0
        while a[j] != auxiliary[i]:
            j += 1
            visualizing.visualize(a, [i, j])
            time.sleep(1 / 20000)
        a[i], a[j] = a[j], a[i]
        visualizing.visualize(a, [i, j])
        time.sleep(1 / 20000)
    auxiliary = []
    return a
