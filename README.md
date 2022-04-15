# Project Name: Radix Sort Machine

## Names of Contributors:

Adrine UWERA
Melissa GIRAMATA
Gabin ISHIMWE
Jessie UMUHIRE UMUTESI
Evelyne UMUBYEYI

## Project description
Sorting algorithms are categorized into comparison-based sorting algorithms and non-comparison-based sorting algorithms.  While comparison-based sorting algorithms are very reliable as they can be used to sort any object since they provide a comparator to define the order, they are slower for sorting large lists, as they have to compare individual elements of the list to come up with a sorted list. For this reason, there is a need for non-comparison-based sorting techniques with a better time-complexity of O(n) compared to comparison-based sorting algorithms with a lower limit of O(n log(n)).

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
