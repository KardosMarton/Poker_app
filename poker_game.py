#!usr/bin/python3

import tkinter as tk
import poker_backend as pb
import os

# Globals
ROUND_COUNTER = 1
#   Default cards global value:
FLOP_CARD_ONE_DEFAULT_TEXT = "FLOP 1"
FLOP_CARD_TWO_DEFAULT_TEXT = "FLOP 2"
FLOP_CARD_THREE_DEFAULT_TEXT = "FLOP 3"
TURN_CARD_DEFAULT_TEXT = "TURN"
RIVER_CARD_DEFAULT_TEXT = "RIVER"
BTN_NEXT_ROUND_TEXT = "NEXT ROUND"
CARD_WIDTH = 17


root = tk.Tk()
root.title('Poker Game')
canvas = tk.Canvas(root, height=400, width=800, bg="blue")
canvas.pack()

IMAGE_BACK_CARD = tk.PhotoImage(file="pictures/back_card.png")

# Test image as background
# filename = tk.PhotoImage(file="pictures/small_club_2.png")
# lbl_test_image = tk.Label(root, image=filename)
# lbl_test_image.place(x=12, y=40)
# Test image as background

lbl_player_one_name = tk.Label(root, text="Juduka").place(x=20, y=20)
# TODO: Create function:  get_selected_card_picture
image_card_one_player_one = tk.PhotoImage(file="{}".format(pb.get_card_image(pb.get_next_card())))
btn_card_one_player_one = tk.Button(root,
                                    # width=CARD_WIDTH,
                                    # text=pb.card_text_format(pb.get_next_card()),
                                    image=image_card_one_player_one,
                                    # bg="black"
                                    )

btn_card_one_player_one.place(x=12, y=40)

image_card_two_player_one = tk.PhotoImage(file="{}".format(pb.get_card_image(pb.get_next_card())))
btn_card_two_player_one = tk.Button(root,
                                    # width=CARD_WIDTH,
                                    # text=pb.card_text_format(pb.get_next_card()),
                                    image=image_card_two_player_one
                                    # bg="black"
                                    )
btn_card_two_player_one.place(x=95, y=40)


lbl_player_two_name = tk.Label(root, text="Marcika").place(x=20, y=160)
image_card_one_player_two = tk.PhotoImage(file="{}".format(pb.get_card_image(pb.get_next_card())))
btn_card_one_player_two = tk.Button(root,
                                    # width=CARD_WIDTH,
                                    # text=pb.card_text_format(pb.get_next_card()),
                                    image=image_card_one_player_two
                                    # bg="black"
                                    )
btn_card_one_player_two.place(x=12, y=180)

image_card_two_player_two = tk.PhotoImage(file="{}".format(pb.get_card_image(pb.get_next_card())))
btn_card_two_player_two = tk.Button(root,
                                    # width=CARD_WIDTH,
                                    # text=pb.card_text_format(pb.get_next_card()),
                                    image=image_card_two_player_two
                                    # bg="black"
                                    )
btn_card_two_player_two.place(x=95, y=180)


# TODO: Add default empty card  picture and set it to flop, turn and river cards.
# Flop cards
btn_flop_card_one = tk.Button(root,
                              image=IMAGE_BACK_CARD,
                              # width=CARD_WIDTH,
                              # text=FLOP_CARD_ONE_DEFAULT_TEXT
                              )
btn_flop_card_one.place(x=270, y=100)

btn_flop_card_two = tk.Button(root,
                              image=IMAGE_BACK_CARD,
                              # width=CARD_WIDTH,
                              # text=FLOP_CARD_TWO_DEFAULT_TEXT
                              )
btn_flop_card_two.place(x=350, y=100)

btn_flop_card_three = tk.Button(root,
                                image=IMAGE_BACK_CARD,
                                # width=CARD_WIDTH,
                                # text=FLOP_CARD_THREE_DEFAULT_TEXT
                                )
btn_flop_card_three.place(x=430, y=100)


# Turn card
btn_turn_card = tk.Button(root,
                          image=IMAGE_BACK_CARD,
                          # width=CARD_WIDTH,
                          # text=TURN_CARD_DEFAULT_TEXT
                          )
btn_turn_card.place(x=530, y=100)


# River card
btn_river_card = tk.Button(root,
                           image=IMAGE_BACK_CARD,
                           # width=CARD_WIDTH,
                           # text=RIVER_CARD_DEFAULT_TEXT
                           )
btn_river_card.place(x=630, y=100)


def get_next_round_cards():
    global ROUND_COUNTER
    print("Burned card: {}".format(pb.get_next_card()))
    if ROUND_COUNTER == 1:
        new_image_flop_one = tk.PhotoImage(file=pb.get_card_image(pb.get_next_card()))
        btn_flop_card_one.configure(image=new_image_flop_one)
        new_image_flop_two = tk.PhotoImage(file=pb.get_card_image(pb.get_next_card()))
        btn_flop_card_two.configure(image=new_image_flop_two)
        new_image_flop_three = tk.PhotoImage(file=pb.get_card_image(pb.get_next_card()))
        btn_flop_card_three.configure(image=new_image_flop_three)
    elif ROUND_COUNTER == 2:
        new_image_turn = tk.PhotoImage(file=pb.get_card_image(pb.get_next_card()))
        btn_turn_card.configure(image=new_image_turn)
    elif ROUND_COUNTER == 3:
        new_image_river = tk.PhotoImage(file=pb.get_card_image(pb.get_next_card()))
        btn_river_card.configure(image=new_image_river)
    ROUND_COUNTER += 1
    root.mainloop()


get_cards = tk.Button(root,
                      width=15,
                      text="Get Cards",
                      command=get_next_round_cards)
get_cards.place(x=270, y=20)


def new_round():
    # Set cards on table to default value
    global IMAGE_BACK_CARD
    btn_flop_card_one.configure(image=IMAGE_BACK_CARD)
    btn_flop_card_two.configure(image=IMAGE_BACK_CARD)
    btn_flop_card_three.configure(image=IMAGE_BACK_CARD)
    btn_turn_card.configure(image=IMAGE_BACK_CARD)
    btn_river_card.configure(image=IMAGE_BACK_CARD)

    # Set global turn value to 1
    global ROUND_COUNTER
    ROUND_COUNTER = 1

    # Generate new card order for cards
    pb.mix_cards()

    # Generate new cards for players
    # Player one cards
    new_image_card_one_player_one = tk.PhotoImage(file="{}".format(pb.get_card_image(pb.get_next_card())))
    btn_card_one_player_one.configure(image=new_image_card_one_player_one)
    new_image_card_two_player_one = tk.PhotoImage(file="{}".format(pb.get_card_image(pb.get_next_card())))
    btn_card_two_player_one.configure(image=new_image_card_two_player_one)
    # Player two cards
    new_image_card_one_player_two = tk.PhotoImage(file="{}".format(pb.get_card_image(pb.get_next_card())))
    btn_card_one_player_two.configure(image=new_image_card_one_player_two)
    new_image_card_two_player_two = tk.PhotoImage(file="{}".format(pb.get_card_image(pb.get_next_card())))
    btn_card_two_player_two.configure(image=new_image_card_two_player_two)
    # btn_card_two_player_two.mainloop()
    root.mainloop()


btn_next_round = tk.Button(root,
                           width=15,
                           text=BTN_NEXT_ROUND_TEXT,
                           command=new_round)
btn_next_round.place(x=270, y=300)

root.mainloop()

# TODO: Replace btn_next_round button
# TODO: Refactor, refactor, refactor
