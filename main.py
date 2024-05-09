from sorting import *
from tools import *

print('WELCOME TO VISUALIZE SORTS\n(A Sorting Algorithm visualizer in your terminal!)\n---VERSION V1.0-alpha---')

length = int(input('Type the length of the array. (Must be an integer): '))
array = visualizing.arrange(length)
visualizing.visualize(array)

sorts = ''

while True:
    sorts = str(input('Type the sorts you want to use. Input \'sorts\' for available sorts. (Must be a string and seperated with commas): '))

    if sorts.lower().replace(' ', '') == 'stop':
        print('Stopped.')
        break

    sorts = useful_tools.string_to_list(sorts.lower().replace(' ', ''))

    for sort in sorts:
        if sort == 'sorts':
            print('AVAILABLE SORTS:\n--- Simple Algorithms ---\nBubble Sort\nInsertion Sort\nSelection Sort\nOdd Even Sort\nBetter Selection Sort\nDouble Better Selection Sort\nComb Sort\n=== Divide and Conquer Algorithms ===\nComing soon...\n--- Joke Algorithms ---\nBogo Sort\nSafe Bogo Sort\nStalin Sort\n=== Made-up Algorithms ===\nGreater Sort')
            break
        if sort == 'bubblesort':
            simple_algorithms.bubblesort(visualizing.shuffle(array))
        elif sort == 'insertionsort':
            simple_algorithms.insertionsort(visualizing.shuffle(array))
        elif sort == 'selectionsort':
            simple_algorithms.selectionsort(visualizing.shuffle(array))
        elif sort == 'oddevensort':
            simple_algorithms.oddevensort(visualizing.shuffle(array))
        elif sort == 'betterselectionsort':
            simple_algorithms.betterselectionsort(visualizing.shuffle(array))
        elif sort == 'doublebetterselectionsort':
            simple_algorithms.doublebetterselectionsort(visualizing.shuffle(array))
        elif sort == 'combsort':
            simple_algorithms.combsort(visualizing.shuffle(array))
        elif sort == 'bogosort':
            joke_algorithms.bogosort(visualizing.shuffle(array))
        elif sort == 'safebogosort':
            joke_algorithms.safebogosort(visualizing.shuffle(array))
        elif sort == 'stalinsort':
            joke_algorithms.stalinsort(visualizing.shuffle(array))
        elif sort == 'greatersort':
            made_up_algorithms.greatersort(visualizing.shuffle(array))

    sorts = ''
