import random
from tkinter import *
import time
from PIL import Image, ImageTk

from pythonds.basic.queue import Queue
import math


delete_img = []


def iteration_cards(cards):
    delete_img = []
    counter = 1
    x = 30
    y = 20
    for i in cards:
        if counter % 13 == 1 and counter != 1:
            y += 80
            x = 30
        img = canvas.create_image(x, y, image=i, anchor=NW)
        delete_img.append(img)
        # time.sleep(1)
        x += 70
        counter += 1
    canvas.after(3000, lambda: [canvas.delete(j) for j in delete_img])


def radix_sort(num_list, redix=10):
    main_bin = Queue()
    bins = {}
    for i in range(redix):
        bins[i] = Queue()

    for num in num_list:
        main_bin.enqueue(num)

    n_digit = math.ceil(math.log(max(num_list), redix))
    index = 0
    y = 600
    for k in range(1, n_digit + 1):
        while not main_bin.isEmpty():
            item = main_bin.dequeue()
            moved_index = num_list.index(item)
            # gain the kth digit of item.
            digit = item % redix ** k // redix ** (k - 1)
            bins[digit].enqueue(item)
            time.sleep(1)
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
            time.sleep(1)
            root.update()
            index += 1

        display_iteration = []
        for j in range(10):
            while not bins[j].isEmpty():
                item1 = bins[j].dequeue()
                resizing_iteration = resize_image(f"images/{str(item1)}.png")
                display_iteration.append(resizing_iteration)
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
                time.sleep(1)
                root.update()

        iteration_cards(display_iteration)

    return main_bin


def resize_image(card):
    open_image = Image.open(card)
    # resize our image
    resize_image = open_image.resize((50, 60))
    our_card_image = ImageTk.PhotoImage(resize_image)
    return our_card_image


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


def open_cards(list_cards):
    # Display all cards
    counter = 1
    x = 30
    y = 20
    for key in keys:
        img = canvas.create_image(x, y, image=allCards[key], anchor=NW)
        displayed_cards.append(img)
        counter += 1

    # Display bin labels
    x_position = 30
    x_prime = 50
    for i in range(0, 10):
        canvas.create_text(x_position, 700, text="bin" + str(i), fill="black", font='Helvetica 15 bold', anchor=SW)
        x_position += 130
        x_prime += 130

    # calling radix sort function
    deck2 = [int(i) for i in keys]
    main_bin = radix_sort(deck2)
    display_sorted(main_bin)


def display_sorted(main_bin):
    canvas.delete("all")
    xPos = 30
    y = 20
    cards_counter = 1
    print(main_bin)
    while not main_bin.isEmpty():
        x = main_bin.dequeue()
        if cards_counter % 4 == 1 and cards_counter != 1:
            xPos += 65
            y = 20
        img = canvas.create_image(xPos, y, image=allCards[str(x)], anchor=NW)
        y += 80
        cards_counter += 1


def cards_layout(dictKeys):
    xPosition = 30
    yPosition = 20
    layout_counter = 1
    for dictKey in dictKeys:
        if layout_counter % 13 == 1 and layout_counter != 1:
            yPosition += 80
            xPosition = 30
        img = canvas.create_image(xPosition, yPosition, image=allCards[dictKey], anchor=NW)
        delete_list.append(img)
        layout_counter += 1
        xPosition += 65
    root.after(3000, lambda: canvas.delete("all"))
    root.after(3000, lambda: open_cards(keys))


root = Tk()
root.title('Cards Radix Sorting')
width = 1450
height = 1000
canvas = Canvas(root, width=width, height=height, bg="green")
canvas.pack()

allCards = {}
displayed_cards = []
delete_list = []

x_card_size = 50
y_card_size = 65
suits = range(1, 5)
values = range(1, 14)
cards()

keys = list(allCards.keys())
random.shuffle(keys)
cards_layout(keys)

root.mainloop()