"""
Radix sorting with card deck animations
------------------------------------------


This is a module that has the methods used  in our program


"""




<<<<<<< HEAD

=======
def iteration_cards(cards):
    """
    A method to iterate through the list of cards image and create the images for every sorting stage

    :param cards: list

    :return: None
    """
    delete_img = []
    counter = 1
    x = 30
    y = 20
    for i in cards:
        if counter % 13 == 1 and counter != 1:
            y += 80
            x = 30
        img = canvas.create_image(x, y, image=i, anchor=NW)  # creating the images
        delete_img.append(img)  # appending the list
        # time.sleep(1)
        x += 70
        counter += 1
        # after some time cards are removed from the
        # screen to start sorting.
    canvas.after(3000, lambda: [canvas.delete(j) for j in delete_img])
>>>>>>> 2529ce03c77460f7de51d7e47e15b6023de156e3



def radix_sort(num_list, redix=10):
    """
    A method that performs the radix sort

    :param num_list: list

    :return:queue
    """
<<<<<<< HEAD
    # main_bin = Queue()
    # bins = {}
    # for i in range(redix):
    #     bins[i] = Queue()
    #
    # for num in num_list:
    #     main_bin.enqueue(num)
    #
    # n_digit = math.ceil(math.log(max(num_list), redix))
    # index = 0
    # # x = [30, 160, 290, 420, 550, 680, 810, 940, 1070, 1200]
    # # x=160
    # y = 600
    # # y1 = 500
    # for k in range(1, n_digit + 1):
    #     while not main_bin.isEmpty():
    #         item = main_bin.dequeue()
    #         moved_index = num_list.index(item)
    #         # gain the kth digit of item.
    #         digit = item % redix ** k // redix ** (k - 1)
    #         # print(digit)
    #
    #         bins[digit].enqueue(item)
    #
    #         if digit == 0:
    #             canvas.move(displayed_cards[moved_index], 0, y)
    #         if digit == 1:
    #             canvas.move(displayed_cards[moved_index], 130, y)
    #         if digit == 2:
    #             canvas.move(displayed_cards[moved_index], 260, y)
    #         if digit == 3:
    #             canvas.move(displayed_cards[moved_index], 390, y)
    #         if digit == 4:
    #             canvas.move(displayed_cards[moved_index], 520, y)
    #         if digit == 5:
    #             canvas.move(displayed_cards[moved_index], 650, y)
    #         if digit == 6:
    #             canvas.move(displayed_cards[moved_index], 780, y)
    #         if digit == 7:
    #             canvas.move(displayed_cards[moved_index], 910, y)
    #         if digit == 8:
    #             canvas.move(displayed_cards[moved_index], 1040, y)
    #         if digit == 9:
    #             canvas.move(displayed_cards[moved_index], 1170, y)
    #         time.sleep(0.1)
    #         root.update()
    #         # y -= 5
    #         # x -= 70
    #         index += 1
    #
    #     for j in range(10):
    #         while not bins[j].isEmpty():
    #             item1 = bins[j].dequeue()
    #             main_bin.enqueue(item1)
    #             moved_index1 = num_list.index(item1)
    #             if j == 0:
    #                 canvas.move(displayed_cards[moved_index1], 0, -y)
    #             elif j == 1:
    #                 canvas.move(displayed_cards[moved_index1], -130, -y)
    #             elif j == 2:
    #                 canvas.move(displayed_cards[moved_index1], -260, -y)
    #             if j == 3:
    #                 canvas.move(displayed_cards[moved_index1], -390, -y)
    #             if j == 4:
    #                 canvas.move(displayed_cards[moved_index1], -520, -y)
    #             if j == 5:
    #                 canvas.move(displayed_cards[moved_index1], -650, -y)
    #             if j == 6:
    #                 canvas.move(displayed_cards[moved_index1], -780, -y)
    #             if j == 7:
    #                 canvas.move(displayed_cards[moved_index1], -910, -y)
    #             if j == 8:
    #                 canvas.move(displayed_cards[moved_index1], -1040, -y)
    #             if j == 9:
    #                 canvas.move(displayed_cards[moved_index1], -1170, -y)
    #             time.sleep(0.1)
    #             root.update()
    #
    # return main_bin
=======
    main_bin = Queue()  # queue to hold the sorted cards(numbers)
    bins = {}  # buckets in which number are sorted from.
    for i in range(redix):
        bins[i] = Queue()  # making each bucket a queue

    for num in num_list:  # adding the cards(numbers) in the queue
        main_bin.enqueue(num)

    n_digit = math.ceil(math.log(max(num_list), redix))
    index = 0
    y = 600
    # performing the sorting
    for k in range(1, n_digit + 1):
        while not main_bin.isEmpty():
            item = main_bin.dequeue()
            moved_index = num_list.index(item)
            # gain the kth digit of item.
            digit = item % redix ** k // redix ** (k - 1)
            bins[digit].enqueue(item)  # adding the card(number) to the respective bin.
            time.sleep(1)
            # moving the cards to their respective bins.
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
        # displaying the cards after each radix-sorting phase
        for j in range(10):
            while not bins[j].isEmpty():
                item1 = bins[j].dequeue()
                resizing_iteration = resize_image(f"images/{str(item1)}.png")
                display_iteration.append(resizing_iteration)
                main_bin.enqueue(item1)
                moved_index1 = num_list.index(item1)
                # moving the cards to their respective bins.

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

        iteration_cards(display_iteration)  # calling the method

    return main_bin  # returning queue
>>>>>>> 2529ce03c77460f7de51d7e47e15b6023de156e3

def resize_image(card):
    """
     A method to resize images used to visualize the cards

     :param card: .png

     :return:.png
     """
<<<<<<< HEAD
    # open_image = Image.open(card)
    # # resize our image
    # resize_image = open_image.resize((50, 60))
    #
    # our_card_image = ImageTk.PhotoImage(resize_image)
    # return our_card_image
=======
    open_image = Image.open(card)
    # resize our image
    resize_image = open_image.resize((50, 60))
    our_card_image = ImageTk.PhotoImage(resize_image)
    return our_card_image
>>>>>>> 2529ce03c77460f7de51d7e47e15b6023de156e3

def cards():
    """
    A method to access images and call resize method

    :return: none
    """
<<<<<<< HEAD
    # suits = [1, 2, 3, 4]
    # values = range(1, 14)
    # global deck
    # deck = []
    # for suit in suits:
    #     for value in values:
    #         deck.append(f"{value}{suit}")
    #
    # for j in deck:
    #     upload = resize_image(f"images/{j}.png")
    #     allCards[j] = upload
=======
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
>>>>>>> 2529ce03c77460f7de51d7e47e15b6023de156e3

def open_cards(list_cards):
    """
    A method to create the cards

    :param list_cards: dictionary

    :return: none
    """

<<<<<<< HEAD
    # counter = 1
    # x = 30
    # y = 20
    # for key in keys:
    #     # if counter % 13 == 1 and counter != 1:
    #     #     # y += 80
    #     #     x = 30
    #     img = canvas.create_image(x, y, image=allCards[key], anchor=NW)
    #     displayed_cards.append(img)
    #     # x += 10
    #     counter += 1
=======
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
    """
     A method to display the sorted cards

    :param main_bin: queue

    :return: None
    """
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

>>>>>>> 2529ce03c77460f7de51d7e47e15b6023de156e3
