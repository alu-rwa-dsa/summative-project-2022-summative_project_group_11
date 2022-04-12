from tkinter import *
import time
from PIL import Image, ImageTk

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
            digit = item % redix**k // redix**(k-1)
            bins[digit].enqueue(item)
        for j in range(10):
            while not bins[j].isEmpty():
                main_bin.enqueue(bins[j].dequeue())
    return main_bin

# def main():
#     a = [552, 431, 26, 531, 736, 2, 777]
#     main_bin = radix_sort(a)
#     while not main_bin.isEmpty():
#         print(main_bin.dequeue())
#
# main()

width = 1450
height = 1000
root = Tk()
canvas = Canvas(root, width=width, height=height, bg="green")
canvas.pack()
photo = PhotoImage(file="images/2_of_clubs.png")
photo1 = PhotoImage(file="images/2_of_hearts.png")
photo_width = photo.width()
photo_height = photo.height()


def resize_image(card):
    open_image = Image.open(card)
    # resize our image
    resize_image = open_image.resize((50, 60))

    our_card_image = ImageTk.PhotoImage(resize_image)
    return our_card_image


x_coords = 0
y_coords = 10
suits = range(1, 5)
values = range(1, 14)
deck1 = []
deck2 = []
for suit in suits:
    for value in values:
        deck1.append(f'{value}{suit}')
        deck2.append(int(str(value) + str(suit)))
x=30
y=20
counter = 1
for i in deck1:
    card = resize_image(f"images/{i}.png")
    card_label = Label(image = card)
    card_label.image = card
    if counter % 13 == 1 and counter != 1:
        y += 80
        x = 30
    card_label.place(x=x,y=y)
    x += 70
    counter +=1

x_position = 30
for i in range(1,11):
    canvas.create_text(x_position, 700, text="bucket"+str(i), fill="black", font=('Helvetica 15 bold'), anchor=SW)
    x_position += 130


# x_velocity = 10
# y_velocity = 10

# Function Call
main_bin = radix_sort(deck2)
while not main_bin.isEmpty():
    print(main_bin.dequeue())

root.mainloop()
