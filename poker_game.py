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


root = tk.Tk()
root.title('Poker Game')
canvas = tk.Canvas(root, height=400, width=800, bg="blue")
canvas.pack()


player_one_name_lbl = tk.Label(root, text="Juduka").place(x=20, y=20)
card_values = pb.get_next_card()
card_one_player_one = tk.Button(root,
                                width=15,
                                text=pb.card_text_format(card_values),
                                bg="black")

card_one_player_one.place(x=12, y=40)
# card_one_player_one.pack()
card_values = pb.get_next_card()
card_two_player_one = tk.Button(root,
                                width=15,
                                text=pb.card_text_format(card_values),
                                bg="black")
# .place(x=12, y=75)
card_two_player_one.place(x=12, y=75)

player_two_name_lbl = tk.Label(root, text="Marcika").place(x=20, y=160)
# card_values = pb.get_next_card()
card_one_player_two = tk.Button(root,
                                width=15,
                                text=pb.card_text_format(pb.get_next_card()),
                                bg="black")
# .place(x=12, y=180)
card_one_player_two.place(x=12, y=180)

# card_values = pb.get_next_card()
card_two_player_two = tk.Button(root,
                                width=15,
                                text=pb.card_text_format(pb.get_next_card()),
                                bg="black")
# .place(x=12, y=215)
card_two_player_two.place(x=12, y=215)

# Button to get flop (1 card to burn, 3 cards to show)
# Add 3 label/button for the 3 cards of flop
flop_card_one = tk.Button(root,
                          width=15,
                          text=FLOP_CARD_ONE_DEFAULT_TEXT)
flop_card_one.place(x=270, y=80)

flop_card_two = tk.Button(root,
                          width=15,
                          text=FLOP_CARD_TWO_DEFAULT_TEXT)
flop_card_two.place(x=270, y=120)

flop_card_three = tk.Button(root,
                            width=15,
                            text=FLOP_CARD_THREE_DEFAULT_TEXT)
flop_card_three.place(x=270, y=160)

turn_card = tk.Button(root,
                      width=15,
                      text=TURN_CARD_DEFAULT_TEXT)
turn_card.place(x=270, y=220)


river_card = tk.Button(root,
                       width=15,
                       text=RIVER_CARD_DEFAULT_TEXT)
river_card.place(x=270, y=260)


def get_next_round_cards():
    global ROUND_COUNTER
    print("Burned card: {}".format(pb.get_next_card()))
    if ROUND_COUNTER == 1:
        flop_card_one.configure(text=pb.card_text_format(pb.get_next_card()))
        flop_card_two.configure(text=pb.card_text_format(pb.get_next_card()))
        flop_card_three.configure(text=pb.card_text_format(pb.get_next_card()))
    elif ROUND_COUNTER == 2:
        turn_card.configure(text=pb.card_text_format(pb.get_next_card()))
    elif ROUND_COUNTER == 3:
        river_card.configure(text=pb.card_text_format(pb.get_next_card()))

    ROUND_COUNTER += 1


get_cards = tk.Button(root,
                      width=15,
                      text="Get Cards",
                      command=get_next_round_cards)
get_cards.place(x=270, y=20)


def new_round():
    # Set cards on table to default value
    flop_card_one.configure(text=FLOP_CARD_ONE_DEFAULT_TEXT)
    flop_card_two.configure(text=FLOP_CARD_TWO_DEFAULT_TEXT)
    flop_card_three.configure(text=FLOP_CARD_THREE_DEFAULT_TEXT)
    turn_card.configure(text=TURN_CARD_DEFAULT_TEXT)
    river_card.configure(text=RIVER_CARD_DEFAULT_TEXT)

    # Set global turn value to 1
    global ROUND_COUNTER
    ROUND_COUNTER = 1

    # Generate new card order for cards
    pb.mix_cards()

    # Generate new cards for players
    # Player one cards
    card_one_player_one.configure(text=pb.card_text_format(pb.get_next_card()))
    card_two_player_one.configure(text=pb.card_text_format(pb.get_next_card()))
    # Player two cards
    card_one_player_two.configure(text=pb.card_text_format(pb.get_next_card()))
    card_two_player_two.configure(text=pb.card_text_format(pb.get_next_card()))


btn_next_round = tk.Button(root,
                           width=15,
                           text=BTN_NEXT_ROUND_TEXT,
                           command=new_round)
btn_next_round.place(x=270, y=300)

root.mainloop()

# TODO: Replace btn_next_round button
# TODO: Refactor, refactor, refactor
