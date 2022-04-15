from queue import Queue
import math


# function that sorts a list using rdaix sort
def radix_sort(num_list, redix=10):
    # initialize the main bin and digit bins.
    main_bin = Queue()
    
    # dictionary to store the sub bins
    bins = {}
    
    # initialize and stores the sub bins into the bins dictionary
    for i in range(redix):
        bins[i] = Queue()
        
    # enqueue the numbers in the passed in list to main bin.
    for num in num_list:
        main_bin.enqueue(num)
        
    # gain the number of digits of the max item in list.
    n_digit = math.ceil(math.log(max(num_list), redix))

    # moves the bins into specific bins according to the digits of the numbers
    for k in range(1, n_digit + 1):
        # iterates to move the numbers into the sub bins
        while not main_bin.isEmpty():
            item = main_bin.dequeue()
            
            # gain the kth digit of item.
            digit = item % redix ** k // redix ** (k - 1)
            
            # stores the number into the sub bin with corresponding digit
            bins[digit].enqueue(item)
            
        # iterates to move the numbers to the main queue
        for j in range(10):
            while not bins[j].isEmpty():
                main_bin.enqueue(bins[j].dequeue())

    # stores the final sorted numbers
    sorted_list = []
    # adds the numbers into the sorted_list array
    while not main_bin.isEmpty():
        item = main_bin.dequeue()
        sorted_list.append(item)
    
    return sorted_list
