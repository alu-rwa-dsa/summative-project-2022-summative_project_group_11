from tkinter import *
import time
from PIL import Image, ImageTk

width=1450
height = 600
root = Tk()
canvas = Canvas(root, width=width, height=height, bg="green")
canvas.pack()
photo = PhotoImage(file="images/2_of_clubs.png")
photo1 = PhotoImage(file="images/2_of_hearts.png")
photo_width = photo.width()
photo_height = photo.height()

card1 = Image.open("images/2_of_hearts.png")
card1_size = card1.resize((80, 80))
card1_main = ImageTk.PhotoImage(card1_size)
my_image1 = canvas.create_image(0, 10, image=card1_main, anchor=NW)

card2 = Image.open("images/2_of_clubs.png")
card2_size = card2.resize((80, 80))
card2_main = ImageTk.PhotoImage(card2_size)
my_image2 = canvas.create_image(85, 10, image=card2_main, anchor=NW)

card3 = Image.open("images/3_of_clubs.png")
card3_size = card3.resize((80, 80))
card3_main = ImageTk.PhotoImage(card3_size)
my_image3 = canvas.create_image(170, 10, image=card3_main, anchor=NW)

card4 = Image.open("images/5_of_clubs.png")
card4_size = card4.resize((80, 80))
card4_main = ImageTk.PhotoImage(card4_size)
my_image4 = canvas.create_image(255, 10, image=card4_main, anchor=NW)

card5 = Image.open("images/6_of_clubs.png")
card5_size = card5.resize((80, 80))
card5_main = ImageTk.PhotoImage(card5_size)
my_image5 = canvas.create_image(340, 10, image=card5_main, anchor=NW)

canvas.create_text(10, 600, text="bucket 1", fill="black", font=('Helvetica 15 bold'), anchor=SW)
canvas.create_text(140, 600, text="bucket 2", fill="black", font=('Helvetica 15 bold'), anchor=SW)
canvas.create_text(240, 600, text="bucket 3", fill="black", font=('Helvetica 15 bold'), anchor=SW)
canvas.create_text(380, 600, text="bucket 4", fill="black", font=('Helvetica 15 bold'), anchor=SW)

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

cardlist = [my_image1, my_image2, my_image3, my_image4, my_image5]
# for i in range(len(cardlist)):
#     if i == 0:
#         canvas.move(cardlist[i], 10, 590-100)
#         time.sleep(1)
#     if i == 1:
#         canvas.move(cardlist[i], 55, 590-100)
i = 0
while True:
    if i == len(cardlist):
        break
    canvas.move(cardlist[i], 10, 590-100)
    root.update()
    time.sleep(1)
    i += 1
root.mainloop()
