from pythonds.basic.queue import Queue
import math


def radix_sort(num_list, redix=10):
    # initialize the main bin and digit bins.
    main_bin = Queue()
    bins = {}
    for i in range(redix):
        bins[i] = Queue()
    # enqueue the number to main bin.
    for num in num_list:
        main_bin.enqueue(num)
    # gain the number of digits of the max item in list.
    n_digit = math.ceil(math.log(max(num_list), redix))

    for k in range(1, n_digit + 1):
        while not main_bin.isEmpty():
            item = main_bin.dequeue()
            # gain the kth digit of item.
            digit = item % redix ** k // redix ** (k - 1)
            bins[digit].enqueue(item)
        for j in range(10):
            while not bins[j].isEmpty():
                main_bin.enqueue(bins[j].dequeue())

    li2 = []
    while not main_bin.isEmpty():
        item = main_bin.dequeue()
        li2.append(item)
    return li2