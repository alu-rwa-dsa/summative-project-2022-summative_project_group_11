# Project Name: Radix Sort Machine

## Names of Contributors:

Adrine UWERA

Melissa GIRAMATA

Gabin ISHIMWE

Jessie UMUHIRE UMUTESI

Evelyne UMUBYEYI




## Solution:

Problem statement:

Sorting algorithms are categorized into comparison-based sorting algorithms and non-comparison-based sorting algorithms.  While comparison-based sorting algorithms are very reliable as they can be used to sort any object since they provide a comparator to define the order, they are slower for sorting large lists, as they have to compare individual elements of the list to come up with a sorted list. For this reason, there is a need for non-comparison-based sorting techniques with a better time-complexity of O(n) compared to comparison-based sorting algorithms with a lower limit of O(n log(n)).

The comparison-based sorting algorithms have O(n log n) or O(n2), and the lower bound of the comparison-based algorithm is Ω(nlogn). This is because any comparison-based sorting algorithm makes at least nlog2 n comparisons to sort the input array as proven by Ford and Johnson using a decision tree diagram. 

These comparison-based sorting algorithms can’t do better than nlogn time complexity. The more efficient sorting is counting sort which is a linear time non-comparison-based sorting algorithm that sorts in O(n+k) time when elements are in the range from 1 to k. (n is the number of items in the original array and k is the range of numbers we could have for every item in the array). Counting sort becomes linear sorting, which is better than comparison-based sorting algorithms that have O(nlogn) time complexity. But when elements are in range 1 to n2, counting sort has O(n2) which is worse than comparison-based sorting algorithms. That’s where the Radix sort comes in as a solution.

The idea of the Radix sort is to extend the counting sort algorithm to get a better time-complexity when k goes n2. The radix sort algorithm does digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort because counting sort is a stable sort. 


The project objectives and contribution :

1.Implementing the radix sorting algorithm to get a better time complexity than the counting sort algorithm.

2.Visualize the background operation of the radix sorting to raise awareness and gain better understanding of what is happening in the program's backend. 

3.Building a backend program for online card games such as solitaire that require sorting cards. This program can be applied in giving hints to players while playing.

4. Apply a sorting technique that removes comparison operations.


Beneficiaries:

1. Online card games can integrate the code to their systems.
2. The program can be used by schools to facilitate teaching of radix sorting
3. General public that wishes to gain insights into the working of radix sort.



## Project description

In this project, we have implemented the radix sorting algorithm, which is a non-comparison-based sorting algorithm for sorting a deck of shuffled playing cards with some animations to help the user understand the technique works in a more engaging way. Radix sort sorts the elements by first grouping the individual digits of the same place value. Then, sort the elements according to their increasing/decreasing order.

We assigned a number value to each card where the last digit represents the suit number given that 1 represents clubs, 2 spades, 3 hearts, and 4 diamonds. The digits before the last one represent the card in this manner:

1 represents an Ace

2 represents 2

3 represents 3

4 represents 4

5 represents 5

6 represents 6

7 represents 7

8 represents 8

9 represents 9

10 represents 10

11 represents a Queen 

12 represents a Jack 

13 represents a King.

So a number like 11 would represent an Ace of clubs, 94 would represent a 9 of diamonds, 123 would represent a jack of hearts, and so on. We will use these assigned values to sort cards as if we were sorting a list of numbers and the program sorts in ascending order.  

This program visualizes how the cards are sorted step by step, by showing how they are moved from the main bin and assigned into bins labelled from 0 to 9 according to the digit they have in a certain place value, and then back to the main bin until they are completely sorted. After the first round of sorting, cards should be sorted according to their suits since the last digit in the cards’ representative number represents their suit clubs should come first, spades second, hearts third, and diamonds last. After the final round of sorting, each column will have four similar cards i.e: the first column will be of aces, the second of  2s, the third of 3s…, and the last will be of Kings.  Each row will also represent a certain suit the first will be of clubs, spades second, hearts third and diamonds last.

## Python Libraries used:

We have used six(6) python libraries in this project. They are as follows:

**Random**: to generate the cards randomly for the first time in order to be sorted <br /> 

**Tkinter**: provides us with the tool for visualizing the sorting i.e., the canvas <br />

**Time**: to time how much time it should take for a card movement to a certain bin <br />

**PIL**: to allow us to use the images of cards on the canvas (GUI) <br />

**Math**: to calculate the number of digits of the numbers that represented the cards <br />

**Pythonds**.basic.queue: to create queues to store the cards as we implement the algorithm. <br />

**Sphinx**: helped us to do the documentation of the project in python and provide us with the preview using the localhost. <br />

Python library that requires installation are:
PIL: Please follow the steps [here](https://blog.finxter.com/how-to-install-pillow-on-pycharm/#:~:text=Select%20your%20current%20project.,quotes%2C%20and%20click%20Install%20Package%20.) to install it first before running the program
Sphinx: Follow the steps [here](https://www.sphinx-doc.org/en/master/usage/installation.html) to install the package in the IDE



## How to run the program:
To use this project, you have to clone it into your local machine and run it in your favourite IDE or text editor.
  
In Pycharm, all one needs to do is to click the play button or right-click and run the program. 


In other Python IDEs, one just runs the program as usual and is able to visualize the algorithm in action.



## Space and Time complexity

# Space:

In this program, we have about 11 Queues,  with a space complexity of O(n*11), we have 1 dictionary with O(n) space complexity,  7 lists with a space complexity of O(n*7), 13 variables with space complexity of O(13), 10 for loops O(11) and 3 while loop with O(3).

O(11n) + O(n) +O(7n)+O(13) + O(11)+O(3)
=O(45n)

===O(n) space complexity.

# Time:

In this program, we have about 11 Queues,  with a time complexity of O(11n) in terms of enqueue and deque, we have 1 dictionary with O(1) time complexity in terms of accessing,  7 lists with time complexity of O(7),  6 for loops with O(6n), two nested loops with O(2n^2) and 1 while loop with O(n).

O(11n) + O(1)+O(7)+O(6n)+O(2n^2)+O(n)
= O(17n)+O(2n^2)+O(8)
=== O(n^2)  time complexity.

# Link to program analysis video: 
https://drive.google.com/file/d/12m6UeVOdp4gjbA6B4RGiDhiitcSyPp4Y/view?usp=sharing

