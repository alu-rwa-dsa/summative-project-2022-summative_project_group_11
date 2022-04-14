import random
from tkinter import *
import time
from PIL import Image, ImageTk
import pythonds
from pythonds.basic.queue import Queue
import math


def radix_sort(num_list, redix=10):
    main_bin = Queue()
    bins = {}
    for i in range(redix):
        bins[i] = Queue()

    for num in num_list:
        main_bin.enqueue(num)

    n_digit = math.ceil(math.log(max(num_list), redix))
    index = 0
    # x = [30, 160, 290, 420, 550, 680, 810, 940, 1070, 1200]
    # x=160
    y = 600
    # y1 = 500
    for k in range(1, n_digit + 1):
        while not main_bin.isEmpty():
            item = main_bin.dequeue()
            moved_index = num_list.index(item)
            # gain the kth digit of item.
            digit = item % redix ** k // redix ** (k - 1)
            # print(digit)

            bins[digit].enqueue(item)

            if digit == 0:
                canvas.move(displayed_cards[moved_index], 0, y)
            if digit == 1:
                canvas.move(displayed_cards[moved_index], 130, y)
            if digit == 2:
                canvas.move(displayed_cards[moved_index], 260, y)
            if digit == 3:
                canvas.move(displayed_cards[moved_index], 390, y)
            if digit == 4:
                canvas.move(displayed_cards[moved_index], 520, y)
            if digit == 5:
                canvas.move(displayed_cards[moved_index], 650, y)
            if digit == 6:
                canvas.move(displayed_cards[moved_index], 780, y)
            if digit == 7:
                canvas.move(displayed_cards[moved_index], 910, y)
            if digit == 8:
                canvas.move(displayed_cards[moved_index], 1040, y)
            if digit == 9:
                canvas.move(displayed_cards[moved_index], 1170, y)
            time.sleep(0.1)
            root.update()
            # y -= 5
            # x -= 70
            index += 1

        for j in range(10):
            while not bins[j].isEmpty():
                item1 = bins[j].dequeue()
                main_bin.enqueue(item1)
                moved_index1 = num_list.index(item1)
                if j == 0:
                    canvas.move(displayed_cards[moved_index1], 0, -y)
                elif j == 1:
                    canvas.move(displayed_cards[moved_index1], -130, -y)
                elif j == 2:
                    canvas.move(displayed_cards[moved_index1], -260, -y)
                if j == 3:
                    canvas.move(displayed_cards[moved_index1], -390, -y)
                if j == 4:
                    canvas.move(displayed_cards[moved_index1], -520, -y)
                if j == 5:
                    canvas.move(displayed_cards[moved_index1], -650, -y)
                if j == 6:
                    canvas.move(displayed_cards[moved_index1], -780, -y)
                if j == 7:
                    canvas.move(displayed_cards[moved_index1], -910, -y)
                if j == 8:
                    canvas.move(displayed_cards[moved_index1], -1040, -y)
                if j == 9:
                    canvas.move(displayed_cards[moved_index1], -1170, -y)
                time.sleep(0.1)
                root.update()

    return main_bin


width = 1450
height = 1000
root = Tk()
canvas = Canvas(root, width=width, height=height, bg="green")
canvas.pack()


def resize_image(card):
    open_image = Image.open(card)
    # resize our image
    resize_image = open_image.resize((50, 60))

    our_card_image = ImageTk.PhotoImage(resize_image)
    return our_card_image


allCards = {}


def cards():
    suits = [1, 2, 3, 4]
    values = range(1, 14)
    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f"{value}{suit}")

    for j in deck:
        upload = resize_image(f"images/{j}.png")
        allCards[j] = upload


cards()
displayed_cards = []


def open_cards(list_cards):
    counter = 1
    x = 30
    y = 20
    for key in keys:
        # if counter % 13 == 1 and counter != 1:
        #     # y += 80
        #     x = 30
        img = canvas.create_image(x, y, image=allCards[key], anchor=NW)
        displayed_cards.append(img)
        # x += 10
        counter += 1


keys = list(allCards.keys())
random.shuffle(keys)
open_cards(keys)

# x_coords = 0
# y_coords = 10
suits = range(1, 5)
values = range(1, 14)

x = 30
y = 20
counter = 1

x_card_size = 50
y_card_size = 65

x_position = 30
x_prime = 50
for i in range(0, 10):
    canvas.create_text(x_position, 700, text="bucket" + str(i), fill="black", font='Helvetica 15 bold', anchor=SW)
    canvas.create_text(x_prime, 730, text=str(i - 1), fill="black", font='Helvetica 15 bold', anchor=SW)
    # print(x_position)
    x_position += 130
    x_prime += 130

# Function Call
deck2 = [int(i) for i in keys]
main_bin = radix_sort(deck2)
sorted_list = []
canvas.delete("all")
xPos = 30
y = 20
cards_counter = 1
while not main_bin.isEmpty():
    x = main_bin.dequeue()
    print(x, type(x))
    # new_card = keys.index(x)
    if cards_counter % 4 == 1 and cards_counter !=1:
        xPos += 65
        y = 20
    img = canvas.create_image(xPos, y, image=allCards[str(x)], anchor=NW)
    y+=80
    cards_counter += 1

root.mainloop()