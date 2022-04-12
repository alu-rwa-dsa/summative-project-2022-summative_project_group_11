from tkinter import *
import time
from PIL import Image, ImageTk

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


x_coords = 0
y_coords = 10
# suits = ["diamonds", "clubs", "hearts", "spades"]
suits = [1, 2, 3, 4]
values = range(2, 15)
deck = []
for suit in suits:
    for value in values:
        deck.append(f"{value}_of_{suit}")
x=30
y=20
counter = 1
for i in deck:
    card = resize_image(f"images/{i}.png")
    card_label = Label(image = card)
    card_label.image = card
    if counter % 13 == 1 and counter != 1:
        y += 80
        x = 30
    card_label.place(x=x,y=y)
    # card_label.grid(column = index, row = 0)
    # if x_coords > width:
    #     my_image2 = canvas.create_image(x_coords, y_coords, image=card, anchor=NW)
    # canvas.create_image(x_coords, y_coords, image=card, anchor=NW)
    # x_coords += 85
    # index +=1
    x += 70
    counter +=1

# card1 = Image.open("images/2_of_hearts.png")
# card1_size = card1.resize((80, 80))
# card1_main = ImageTk.PhotoImage(card1_size)
# my_image1 = canvas.create_image(0, 10, image=card1_main, anchor=NW)
#
# card2 = Image.open("images/2_of_clubs.png")
# card2_size = card2.resize((80, 80))
# card2_main = ImageTk.PhotoImage(card2_size)
# my_image2 = canvas.create_image(85, 10, image=card2_main, anchor=NW)
#
# card3 = Image.open("images/3_of_clubs.png")
# card3_size = card3.resize((80, 80))
# card3_main = ImageTk.PhotoImage(card3_size)
# my_image3 = canvas.create_image(170, 10, image=card3_main, anchor=NW)
#
# card4 = Image.open("images/5_of_clubs.png")
# card4_size = card4.resize((80, 80))
# card4_main = ImageTk.PhotoImage(card4_size)
# my_image4 = canvas.create_image(255, 10, image=card4_main, anchor=NW)
#
# card5 = Image.open("images/6_of_clubs.png")
# card5_size = card5.resize((80, 80))
# card5_main = ImageTk.PhotoImage(card5_size)
# my_image5 = canvas.create_image(340, 10, image=card5_main, anchor=NW)

x_position = 30
for i in range(1,11):
    canvas.create_text(x_position, 700, text="bucket"+str(i), fill="black", font=('Helvetica 15 bold'), anchor=SW)
    x_position += 130


x_velocity = 10
y_velocity = 10
# while True:
#     coordinates = canvas.coords(my_image3)
#     print(coordinates)
#     # if coordinates[0] >= width - photo_width:
#     #     x_velocity *= -1
#     #
#     # if coordinates[1] >= height - photo_height:
#     #     y_velocity *= -1
#     # if canvas.coords(my_image3)[0] == 240 and canvas.coords(my_image3)[1] == 450:
#     #     break
#     canvas.move(my_image3, 70, 490)
#     root.update()
#     time.sleep(1)
#     break

# cardlist = [my_image1, my_image2, my_image3, my_image4, my_image5]
# for i in range(len(cardlist)):
#     if i == 0:
#         canvas.move(cardlist[i], 10, 590-100)
#         time.sleep(1)
#     if i == 1:
#         canvas.move(cardlist[i], 55, 590-100)
# i = 0
# y = 590-100
# while True:
#     if i == len(cardlist):
#         break
#     canvas.move(cardlist[i], x_velocity, y)
#     root.update()
#     time.sleep(1)
#     y -= 10
#     x_velocity -= 85
#     i += 1
root.mainloop()
