"""A singleplayer tic tac toe game against an AI that uses the unbeatable strategy.
This AI doesn't always win, but it never loses.
The AI uses the technique shown in these articles:
https://www.wikihow.com/Win-at-Tic-Tac-Toe#:~:text=Play%20your%20first%20X%20in,you%20can%20guarantee%20a%20win.
https://mathwithbaddrawings.com/2013/06/16/ultimate-tic-tac-toe/

See my handwritten notes for a full visual map of the decision tree.
"""

import random
import time
import tkinter
from tkinter import messagebox

# Development steps:
# TODO: Indicate whose turn it is.
# TODO: Make the UI pretty by tinkering with reliefs, frames, etc.
# TODO: Add music that crossfades between 2 tracks, depending on whether it's your turn or the AI's.
# TODO: Get buttons to stop wiggling when their text content changes.
# TODO: Eliminate redundant calls of rotate_lists_of_lists.

# Randomly decide whether you're X or 0.
if random.randint(0, 1) == 1:
    player_x_or_o = "X"
    ai_x_or_o = "O"
    player_turn = True
else:
    player_x_or_o = "O"
    ai_x_or_o = "X"
    player_turn = False

turn_counter = 0    # To indicate that it's the first turn.
game_state = []     # Helps the AI efficiently keep track of the game state and make decisions.
ccw_board_rotations_from_actual_to_model = 0    # Helps the AI rotate its interpretation of the board state.


# Functions
def player_mark(button_to_change):
    """Marks the button clicked with the player's symbol."""
    global player_turn
    global turn_counter
    if player_turn and button_to_change["text"] == " ":     # You can get any option of any widget this way.
        button_to_change.config(text=player_x_or_o)
        check_for_win("player")
        turn_counter = turn_counter + 1     # Increment the turn counter.
        player_turn = not player_turn   # Finally, invert whose turn it is.
        ai_mark()   # AI takes a turn.


def ai_mark():
    """Uses an AI decision tree to choose and mark a button with the AI's symbol."""
    global player_turn
    global turn_counter
    global game_state
    global ccw_board_rotations_from_actual_to_model
    space_statuses = [[button_corner_topleft["text"], button_side_top["text"], button_corner_topright["text"]],
                      [button_side_left["text"], button_center["text"], button_side_right["text"]],
                      [button_corner_bottomleft["text"], button_side_bottom["text"], button_corner_bottomright["text"]]]
    time.sleep(0)   # Imply that the AI is taking time to think, and build suspense.

    # AI marks a square with the unbeatable strategy linked in main's docstring.
    # IF AI GOES FIRST:
    if turn_counter == 0:   # If it's the AI's first turn and the AI is playing first:
        button_corner_bottomleft.config(text=ai_x_or_o)
        game_state = [0, 0]

    elif turn_counter == 2:     # If it's the AI's second turn and the AI played first:
        if button_side_left["text"] == player_x_or_o:
            button_corner_bottomright.config(text=ai_x_or_o)
            game_state = [2, 0]
        elif button_side_bottom["text"] == player_x_or_o:
            button_corner_topleft.config(text=ai_x_or_o)
            game_state = [2, 1]
        elif button_side_top["text"] == player_x_or_o:
            button_corner_topleft.config(text=ai_x_or_o)
            game_state = [2, 2]
        elif button_side_right["text"] == player_x_or_o:
            button_corner_bottomright.config(text=ai_x_or_o)
            game_state = [2, 3]
        elif button_corner_topleft["text"] == player_x_or_o:
            button_corner_bottomright.config(text=ai_x_or_o)
            game_state = [2, 4]
        elif button_corner_topright["text"] == player_x_or_o:
            button_corner_bottomright.config(text=ai_x_or_o)
            game_state = [2, 5]
        elif button_corner_bottomright["text"] == player_x_or_o:
            button_corner_topleft.config(text=ai_x_or_o)
            game_state = [2, 6]
        elif button_center["text"] == player_x_or_o:
            button_corner_topright.config(text=ai_x_or_o)
            game_state = [2, 7]

    elif turn_counter == 4:     # If it's the AI's third turn and the AI played first:
        # If player didn't take the center on Turn 1:
        if game_state == [2, 0]:
            if button_side_bottom["text"] == player_x_or_o:
                button_corner_topright.config(text=ai_x_or_o)   # Set up a trap.
                game_state = [4, 0]
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
        elif game_state == [2, 1]:
            if button_side_left["text"] == player_x_or_o:
                button_corner_topright.config(text=ai_x_or_o)   # Set up a trap.
                game_state = [4, 1]
            else:
                button_side_left.config(text=ai_x_or_o)     # Win.
        elif game_state == [2, 2]:
            if button_side_left["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)    # Set up a trap.
                game_state = [4, 2]
            else:
                button_side_left.config(text=ai_x_or_o)     # Win.
        elif game_state == [2, 3]:
            if button_side_bottom["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)    # Set up a trap.
                game_state = [4, 3]
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
        elif game_state == [2, 4]:
            if button_side_bottom["text"] == player_x_or_o:
                button_corner_topright.config(text=ai_x_or_o)   # Set up a trap.
                game_state = [4, 4]
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
        elif game_state == [2, 5]:
            if button_side_bottom["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)    # Set up a trap.
                game_state = [4, 5]
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
        elif game_state == [2, 6]:
            if button_side_left["text"] == player_x_or_o:
                button_corner_topright.config(text=ai_x_or_o)   # Set up a trap.
                game_state = [4, 6]
            else:
                button_side_left.config(text=ai_x_or_o)     # Win.
        # If player took the center on Turn 1:
        elif game_state == [2, 7]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)    # Set up a trap.
                game_state = [4, 7]
            elif button_corner_bottomright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)    # set up a trap.
                game_state = [4, 8]
            elif button_side_top["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)
                game_state = [4, 9]
            elif button_side_right["text"] == player_x_or_o:
                button_side_left.config(text=ai_x_or_o)
                game_state = [4, 10]
            elif button_side_bottom["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)
                game_state = [4, 11]
            elif button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)
                game_state = [4, 12]

    elif turn_counter == 6:     # If it's the AI's fourth turn and the AI played first:
        # If the player didn't take the center on Turn 1:
        if game_state == [4, 0]:
            if button_center["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)    # Win.
            else:
                button_center.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 1]:
            if button_center["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)  # Win.
            else:
                button_center.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 2]:
            if button_center["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
            else:
                button_center.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 3]:
            if button_center["text"] == player_x_or_o:
                button_side_left.config(text=ai_x_or_o)     # Win.
            else:
                button_center.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 4]:
            if button_center["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)    # Win.
            else:
                button_center.config(text=ai_x_or_o)     # Win.
        elif game_state == [4, 5]:
            if button_center["text"] == player_x_or_o:
                button_side_left.config(text=ai_x_or_o)     # Win.
            else:
                button_center.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 6]:
            if button_center["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)  # Win.
            else:
                button_center.config(text=ai_x_or_o)    # Win.
        # If the player took the center on Turn 1:
        elif game_state == [4, 7]:
            if button_side_right["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
            else:
                button_side_right.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 8]:
            if button_side_left["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)  # Win.
            else:
                button_side_left.config(text=ai_x_or_o)     # Win.
        elif game_state == [4, 9]:
            if button_corner_bottomright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)
                game_state = [6, 0]
            else:
                button_corner_bottomright.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 10]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)
                game_state = [6, 1]
            else:
                button_corner_topleft.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 11]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)
                game_state = [6, 2]
            else:
                button_corner_topleft.config(text=ai_x_or_o)    # Win.
        elif game_state == [4, 12]:
            if button_corner_bottomright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)
                game_state = [6, 3]
            else:
                button_corner_bottomright.config(text=ai_x_or_o)    # Win.

    elif turn_counter == 8:     # If it's the AI's fifth turn and the AI played first:
        if game_state == [6, 0]:
            if button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)    # Tie.
            else:
                button_side_left.config(text=ai_x_or_o)     # Win.
        if game_state == [6, 1]:
            if button_side_bottom["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)      # Tie.
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
        if game_state == [6, 2]:
            if button_side_right["text"] == player_x_or_o:
                button_side_left.config(text=ai_x_or_o)     # Tie.
            else:
                button_side_right.config(text=ai_x_or_o)    # Win.
        if game_state == [6, 3]:
            if button_side_top["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)   # Tie.
            else:
                button_side_top.config(text=ai_x_or_o)      # Win.

    # IF AI GOES SECOND
    elif turn_counter == 1:   # If it's the AI's first turn and the player is playing first:
        # If player went center:
        if button_center["text"] == player_x_or_o:
            button_corner_bottomleft.config(text=ai_x_or_o)
            game_state = [1, 0]
        # If player went corner (rotation needed):
        elif button_corner_bottomleft["text"] == player_x_or_o:
            ccw_board_rotations_from_actual_to_model = 0
            button_center.config(text=ai_x_or_o)
            game_state = [11, 0]
        elif button_corner_topleft["text"] == player_x_or_o:
            ccw_board_rotations_from_actual_to_model = 1
            button_center.config(text=ai_x_or_o)
            game_state = [11, 0]
        elif button_corner_topright["text"] == player_x_or_o:
            ccw_board_rotations_from_actual_to_model = 2
            button_center.config(text=ai_x_or_o)
            game_state = [11, 0]
        elif button_corner_bottomright["text"] == player_x_or_o:
            ccw_board_rotations_from_actual_to_model = 3
            button_center.config(text=ai_x_or_o)
            game_state = [11, 0]
        # If player went side (rotation needed):
        elif button_side_left["text"] == player_x_or_o:
            ccw_board_rotations_from_actual_to_model = 0
            button_center.config(text=ai_x_or_o)
            game_state = [21, 0]
        elif button_side_top["text"] == player_x_or_o:
            ccw_board_rotations_from_actual_to_model = 1
            button_center.config(text=ai_x_or_o)
            game_state = [21, 0]
        elif button_side_right["text"] == player_x_or_o:
            ccw_board_rotations_from_actual_to_model = 2
            button_center.config(text=ai_x_or_o)
            game_state = [21, 0]
        elif button_side_bottom["text"] == player_x_or_o:
            ccw_board_rotations_from_actual_to_model = 3
            button_center.config(text=ai_x_or_o)
            game_state = [21, 0]

    elif turn_counter == 3:  # If it's the AI's second turn and the player is playing first:
        # If player went center on their first turn:
        if game_state == [1, 0]:
            if button_corner_topright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)
                game_state = [3, 0]
            elif button_side_top["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)
                game_state = [3, 1]
            elif button_side_right["text"] == player_x_or_o:
                button_side_left.config(text=ai_x_or_o)
                game_state = [3, 2]
            elif button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)
                game_state = [3, 3]
            elif button_corner_bottomright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)
                game_state = [3, 4]
            elif button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)
                game_state = [3, 5]
            elif button_side_bottom["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)
                game_state = [3, 6]
        # If player went corner on their first turn (rotation needed):
        elif game_state == [11, 0]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[1][0] == player_x_or_o:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)
                game_state = [13, 0]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][1] == player_x_or_o:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)
                game_state = [13, 1]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][0] == player_x_or_o:
                ai_rotated_response("button_side_left", ccw_board_rotations_from_actual_to_model)
                game_state = [13, 2]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)
                game_state = [13, 3]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][1] == player_x_or_o:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)
                game_state = [13, 4]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[1][2] == player_x_or_o:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)
                game_state = [13, 5]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][2] == player_x_or_o:
                ai_rotated_response("button_side_top", ccw_board_rotations_from_actual_to_model)
                game_state = [13, 6]
        # If player went side on their first turn (rotation needed):
        elif game_state == [21, 0]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][0] == player_x_or_o:
                ai_rotated_response("button_corner_bottomleft", ccw_board_rotations_from_actual_to_model)
                game_state = [23, 0]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][0] == player_x_or_o:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)
                game_state = [23, 1]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][1] == player_x_or_o:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)
                game_state = [23, 2]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][1] == player_x_or_o:
                ai_rotated_response("button_corner_bottomleft", ccw_board_rotations_from_actual_to_model)
                game_state = [23, 3]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][2] == player_x_or_o:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)
                game_state = [23, 4]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_corner_bottomleft", ccw_board_rotations_from_actual_to_model)
                game_state = [23, 5]
            elif rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[1][2] == player_x_or_o:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)
                game_state = [23, 6]

    elif turn_counter == 5:  # If it's the AI's third turn and the player is playing first:
        # If player went center on their first turn:
        if game_state == [3, 0]:
            if button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)
                game_state = [5, 0]
            else:
                button_side_left.config(text=ai_x_or_o)     # Win.
        elif game_state == [3, 1]:
            if button_corner_bottomright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)
                game_state = [5, 1]
            else:
                button_corner_bottomright.config(text=ai_x_or_o)    # Win.
        elif game_state == [3, 2]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)
                game_state = [5, 2]
            else:
                button_corner_topleft.config(text=ai_x_or_o)     # Win.
        elif game_state == [3, 3]:
            if button_side_bottom["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)
                game_state = [5, 3]
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
        elif game_state == [3, 4]:
            if button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)
                game_state = [5, 4]
            else:
                button_side_left.config(text=ai_x_or_o)     # Win.
        elif game_state == [3, 5]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)
                game_state = [5, 5]
            elif button_side_top["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)
                game_state = [5, 6]
            elif button_corner_topright["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)
                game_state = [5, 7]
            elif button_side_bottom["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)
                game_state = [5, 8]
            elif button_corner_bottomright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)
                game_state = [5, 9]
        elif game_state == [3, 6]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)
                game_state = [5, 10]
            elif button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)
                game_state = [5, 11]
            elif button_corner_topright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)
                game_state = [5, 12]
            elif button_side_right["text"] == player_x_or_o:
                button_side_left.config(text=ai_x_or_o)
                game_state = [5, 13]
            elif button_corner_bottomright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)
                game_state = [5, 14]
        # If player went corner on their first turn (rotation needed):
        elif game_state == [13, 0]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)
                game_state = [15, 0]
            else:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [13, 1]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][0] == player_x_or_o:
                ai_rotated_response("button_side_left", ccw_board_rotations_from_actual_to_model)
                game_state = [15, 1]
            else:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [13, 2]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[1][2] == player_x_or_o:
                ai_rotated_response("button_side_top", ccw_board_rotations_from_actual_to_model)
                game_state = [15, 2]
            else:
                ai_rotated_response("button_side_right", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [13, 3]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][1] == player_x_or_o:
                ai_rotated_response("button_side_left", ccw_board_rotations_from_actual_to_model)
                game_state = [15, 3]
            else:
                ai_rotated_response("button_side_top", ccw_board_rotations_from_actual_to_model)    # Win.
        elif game_state == [13, 4]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)
                game_state = [15, 4]
            else:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)   # Win.
        elif game_state == [13, 5]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][0] == player_x_or_o:
                ai_rotated_response("button_side_left", ccw_board_rotations_from_actual_to_model)
                game_state = [15, 5]
            else:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [13, 6]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][1] == player_x_or_o:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)
                game_state = [15, 6]
            else:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)     # Win.
        # If player went side on their first turn (rotation needed):
        elif game_state == [23, 0]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][2] == player_x_or_o:
                ai_rotated_response("button_side_top", ccw_board_rotations_from_actual_to_model)
                game_state = [25, 0]
            else:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Win.
        elif game_state == [23, 1]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)
                game_state = [25, 1]
            else:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)   # Win.
        elif game_state == [23, 2]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_corner_bottomleft", ccw_board_rotations_from_actual_to_model)
                game_state = [25, 2]
            else:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [23, 3]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][2] == player_x_or_o:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)
                game_state = [25, 3]
            else:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Win.
        elif game_state == [23, 4]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_side_right", ccw_board_rotations_from_actual_to_model)
                game_state = [25, 4]
            else:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [23, 5]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][2] == player_x_or_o:
                ai_rotated_response("button_side_right", ccw_board_rotations_from_actual_to_model)
                game_state = [25, 5]
            else:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Win.
        elif game_state == [23, 6]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)
                game_state = [25, 6]
            else:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)  # Win.

    elif turn_counter == 7:  # If it's the AI's fourth turn and the player is playing first:
        # If player went center on their first turn:
        if game_state == [5, 0]:
            if button_side_top["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)   # Tie.
            else:
                button_side_top.config(text=ai_x_or_o)      # Tie.
        elif game_state == [5, 1]:
            if button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)    # Tie.
            else:
                button_side_left.config(text=ai_x_or_o)     # Tie.
        elif game_state == [5, 2]:
            if button_side_bottom["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)      # Tie.
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Tie.
        elif game_state == [5, 3]:
            if button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)    # Tie.
            else:
                button_side_left.config(text=ai_x_or_o)     # Tie.
        elif game_state == [5, 4]:
            if button_side_top["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)   # Tie.
            else:
                button_side_top.config(text=ai_x_or_o)      # Tie.
        elif game_state == [5, 5]:
            if button_side_bottom["text"] == player_x_or_o:
                button_corner_topright.config(text=ai_x_or_o)   # Win.
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
        elif game_state == [5, 6]:
            if button_corner_bottomright["text"] == player_x_or_o:
                button_corner_topleft.config(text=ai_x_or_o)    # Tie.
            else:
                button_corner_bottomright.config(text=ai_x_or_o)    # Win.
        elif game_state == [5, 7]:
            if button_side_bottom["text"] == player_x_or_o:
                button_side_top.config(text=ai_x_or_o)  # Tie.
            else:
                button_side_bottom.config(text=ai_x_or_o)   # Win.
        elif game_state == [5, 8]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)    # Tie.
            else:
                button_corner_topleft.config(text=ai_x_or_o)    # Tie.
        elif game_state == [5, 9]:
            if button_side_top["text"] == player_x_or_o:
                button_side_bottom.config(text=ai_x_or_o)   # Tie.
            else:
                button_side_top.config(text=ai_x_or_o)  # Tie.
        elif game_state == [5, 10]:
            if button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)    # Tie.
            else:
                button_side_left.config(text=ai_x_or_o)     # Tie.
        elif game_state == [5, 11]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)    # Tie.
            else:
                button_corner_topleft.config(text=ai_x_or_o)    # Tie.
        elif game_state == [5, 12]:
            if button_side_left["text"] == player_x_or_o:
                button_side_right.config(text=ai_x_or_o)    # Tie.
            else:
                button_side_left.config(text=ai_x_or_o)     # Win.
        elif game_state == [5, 13]:
            if button_corner_topleft["text"] == player_x_or_o:
                button_corner_bottomright.config(text=ai_x_or_o)    # Tie.
            else:
                button_corner_topleft.config(text=ai_x_or_o)    # Win.
        elif game_state == [5, 14]:
            if button_side_left["text"] == player_x_or_o:
                button_corner_topright.config(text=ai_x_or_o)
            else:
                button_side_left.config(text=ai_x_or_o)
        # If player went corner on their first turn (rotation needed):
        elif game_state == [15, 0]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][1] == player_x_or_o:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Tie.
            else:
                ai_rotated_response("button_side_top", ccw_board_rotations_from_actual_to_model)    # Win.
        elif game_state == [15, 1]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[1][2] == player_x_or_o:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Tie.
            else:
                ai_rotated_response("button_side_right", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [15, 2]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][1] == player_x_or_o:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)  # Tie.
            else:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)     # Win.
        elif game_state == [15, 3]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[1][2] == player_x_or_o:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Tie.
            else:
                ai_rotated_response("button_side_right", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [15, 4]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][2] == player_x_or_o:
                ai_rotated_response("button_side_right", ccw_board_rotations_from_actual_to_model)  # Tie.
            else:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Tie.
        elif game_state == [15, 5]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][2] == player_x_or_o:
                ai_rotated_response("button_side_top", ccw_board_rotations_from_actual_to_model)    # Tie.
            else:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Tie.
        elif game_state == [15, 6]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][0] == player_x_or_o:
                ai_rotated_response("button_side_left", ccw_board_rotations_from_actual_to_model)
            else:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)
        # If player went side on their first turn (rotation needed):
        elif game_state == [25, 0]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][1] == player_x_or_o:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)  # Tie.
            else:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)     # Win.
        elif game_state == [25, 1]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][1] == player_x_or_o:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Tie.
            else:
                ai_rotated_response("button_side_top", ccw_board_rotations_from_actual_to_model)    # Win.
        elif game_state == [25, 2]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][2] == player_x_or_o:
                ai_rotated_response("button_side_right", ccw_board_rotations_from_actual_to_model)  # Tie.
            else:
                ai_rotated_response("button_corner_topright", ccw_board_rotations_from_actual_to_model)     # Win.
        elif game_state == [25, 3]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][2] == player_x_or_o:
                ai_rotated_response("button_side_right", ccw_board_rotations_from_actual_to_model)  # Tie.
            else:
                ai_rotated_response("button_corner_bottomright", ccw_board_rotations_from_actual_to_model)  # Win.
        elif game_state == [25, 4]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][0] == player_x_or_o:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)     # Tie.
            else:
                ai_rotated_response("button_corner_bottomleft", ccw_board_rotations_from_actual_to_model)   # Tie.
        elif game_state == [25, 5]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[0][0] == player_x_or_o:
                ai_rotated_response("button_side_top", ccw_board_rotations_from_actual_to_model)    # Tie.
            else:
                ai_rotated_response("button_corner_topleft", ccw_board_rotations_from_actual_to_model)  # Tie.
        elif game_state == [25, 6]:
            if rotate_list_of_lists(space_statuses, ccw_board_rotations_from_actual_to_model)[2][0] == player_x_or_o:
                ai_rotated_response("button_side_bottom", ccw_board_rotations_from_actual_to_model)     # Tie.
            else:
                ai_rotated_response("button_corner_bottomleft", ccw_board_rotations_from_actual_to_model)   # Win.

    check_for_win("ai")
    turn_counter = turn_counter + 1     # Increment the turn counter.
    player_turn = not player_turn   # Finally, invert whose turn it is.


def check_for_win(team):
    """Checks to see if the given team ('player' or 'ai') has 3 in a row, vertically, horizontally, or diagonally.
    If so, calls the function announce_win.
    """
    rows_of_3 = [[button_corner_topleft["text"], button_side_top["text"], button_corner_topright["text"]],
                 [button_side_left["text"], button_center["text"], button_side_right["text"]],
                 [button_corner_bottomleft["text"], button_side_bottom["text"], button_corner_bottomright["text"]]]
    columns_of_3 = [[button_corner_topleft["text"], button_side_left["text"], button_corner_bottomleft["text"]],
                    [button_side_top["text"], button_center["text"], button_side_bottom["text"]],
                    [button_corner_topright["text"], button_side_right["text"], button_corner_bottomright["text"]]]
    diagonals_of_3 = [[button_corner_topleft["text"], button_center["text"], button_corner_bottomright["text"]],
                      [button_corner_bottomleft["text"], button_center["text"], button_corner_topright["text"]]]
    if team == "player":
        player_streak = [player_x_or_o, player_x_or_o, player_x_or_o]   # If this appears as an element of
        # rows/columns/diagonals of 3, then the player has won.
        if (player_streak in rows_of_3) or (player_streak in columns_of_3) or (player_streak in diagonals_of_3):
            announce_win("player")
    elif team == "ai":
        ai_streak = [ai_x_or_o, ai_x_or_o, ai_x_or_o]   # If this appears as an element of rows/columns/diagonals of 3,
        # then the player has won.
        if (ai_streak in rows_of_3) or (ai_streak in columns_of_3) or (ai_streak in diagonals_of_3):
            announce_win("ai")
    else:
        raise ValueError("team must equal 'player' or 'ai'")
    if turn_counter >= 8:
        announce_win("tie")


def announce_win(team):
    """Show a messagebox announcing that the input team ('player' or 'ai') has won, then close the game."""
    if team == "player":
        messagebox.showinfo("GAME!", "You win!")
        board.destroy()
        exit()
    elif team == "ai":
        messagebox.showinfo("GAME!", "You lose. :(")
        board.destroy()
        exit()
    elif team == "tie":
        messagebox.showinfo("GAME!", "Tie!  Well played indeed.")
        board.destroy()
        exit()
    else:
        raise ValueError("team must equal 'player', 'ai', or 'tie'")


def rotate_list_of_lists(list_of_lists, rotations_ccw):
    """Rotates the given list of lists.  rotations_ccw should be a positive integer representing the number of ccw
    rotations desired for the list of lists.
    Assumes an nxn list of lists.
    """
    for turn in range(rotations_ccw):   # In each iteration, set lists_of_lists equal to itself rotated 90 degrees ccw.
        temp_list_of_lists = list_of_lists
        # Create list of columns from right to left.
        list_of_columns = []
        for current_column in reversed(range(len(temp_list_of_lists[0]))):
            column = []
            for current_row in range(len(temp_list_of_lists[0])):
                column.append(temp_list_of_lists[current_row][current_column])
            list_of_columns.append(column)
        list_of_lists = list_of_columns
    return list_of_lists


def ai_rotated_response(target_button, rotations_cw):
    """Mark the appropriate space after rotating the desired number of turns CLOCKWISE.  Assumes a 3x3 grid.
    target_button must be a string.  rotations_cw must be an integer from 0 to 3.
    """
    if type(rotations_cw) != int:
        raise TypeError("rotations_cw must be an integer from 0 to 3.")
    if not(rotations_cw in [0, 1, 2, 3]):
        raise ValueError("rotations_cw must be an integer from 0 to 3.")

    if target_button == "button_center":
        button_center.config(text=ai_x_or_o)
    elif target_button == "button_side_top":
        if rotations_cw == 0:
            button_side_top.config(text=ai_x_or_o)
        elif rotations_cw == 1:
            button_side_right.config(text=ai_x_or_o)
        elif rotations_cw == 2:
            button_side_bottom.config(text=ai_x_or_o)
        elif rotations_cw == 3:
            button_side_left.config(text=ai_x_or_o)
    elif target_button == "button_side_right":
        if rotations_cw == 0:
            button_side_right.config(text=ai_x_or_o)
        elif rotations_cw == 1:
            button_side_bottom.config(text=ai_x_or_o)
        elif rotations_cw == 2:
            button_side_left.config(text=ai_x_or_o)
        elif rotations_cw == 3:
            button_side_top.config(text=ai_x_or_o)
    elif target_button == "button_side_bottom":
        if rotations_cw == 0:
            button_side_bottom.config(text=ai_x_or_o)
        elif rotations_cw == 1:
            button_side_left.config(text=ai_x_or_o)
        elif rotations_cw == 2:
            button_side_top.config(text=ai_x_or_o)
        elif rotations_cw == 3:
            button_side_right.config(text=ai_x_or_o)
    elif target_button == "button_side_left":
        if rotations_cw == 0:
            button_side_left.config(text=ai_x_or_o)
        elif rotations_cw == 1:
            button_side_top.config(text=ai_x_or_o)
        elif rotations_cw == 2:
            button_side_right.config(text=ai_x_or_o)
        elif rotations_cw == 3:
            button_side_bottom.config(text=ai_x_or_o)
    elif target_button == "button_corner_topleft":
        if rotations_cw == 0:
            button_corner_topleft.config(text=ai_x_or_o)
        elif rotations_cw == 1:
            button_corner_topright.config(text=ai_x_or_o)
        elif rotations_cw == 2:
            button_corner_bottomright.config(text=ai_x_or_o)
        elif rotations_cw == 3:
            button_corner_bottomleft.config(text=ai_x_or_o)
    elif target_button == "button_corner_topright":
        if rotations_cw == 0:
            button_corner_topright.config(text=ai_x_or_o)
        elif rotations_cw == 1:
            button_corner_bottomright.config(text=ai_x_or_o)
        elif rotations_cw == 2:
            button_corner_bottomleft.config(text=ai_x_or_o)
        elif rotations_cw == 3:
            button_corner_topleft.config(text=ai_x_or_o)
    elif target_button == "button_corner_bottomright":
        if rotations_cw == 0:
            button_corner_bottomright.config(text=ai_x_or_o)
        elif rotations_cw == 1:
            button_corner_bottomleft.config(text=ai_x_or_o)
        elif rotations_cw == 2:
            button_corner_topleft.config(text=ai_x_or_o)
        elif rotations_cw == 3:
            button_corner_topright.config(text=ai_x_or_o)
    elif target_button == "button_corner_bottomleft":
        if rotations_cw == 0:
            button_corner_bottomleft.config(text=ai_x_or_o)
        elif rotations_cw == 1:
            button_corner_topleft.config(text=ai_x_or_o)
        elif rotations_cw == 2:
            button_corner_topright.config(text=ai_x_or_o)
        elif rotations_cw == 3:
            button_corner_bottomright.config(text=ai_x_or_o)
    else:
        raise ValueError("target_button must be a string: button_center, button_side_top, button_side_right, "
                         "button_side_bottom, button_side_left, button_corner_topleft, button_corner_topright, "
                         "button_corner_bottomright, button_corner_bottomleft")


# Create a 3x3 grid of buttons.
board = tkinter.Tk()
board.title("Tic Tac Toe: You're " + player_x_or_o + "!")
board.geometry("300x300")
for x in range(3):
    tkinter.Grid.columnconfigure(board, x, weight=1)
for y in range(3):
    tkinter.Grid.rowconfigure(board, y, weight=1)

button_corner_topleft = tkinter.Button(board, text=" ", command=lambda: player_mark(button_corner_topleft))
button_corner_topleft.grid(row=0, column=0)

button_side_top = tkinter.Button(board, text=" ", command=lambda: player_mark(button_side_top))
button_side_top.grid(row=0, column=1)

button_corner_topright = tkinter.Button(board, text=" ", command=lambda: player_mark(button_corner_topright))
button_corner_topright.grid(row=0, column=2)

button_side_left = tkinter.Button(board, text=" ", command=lambda: player_mark(button_side_left))
button_side_left.grid(row=1, column=0)

button_center = tkinter.Button(board, text=" ", command=lambda: player_mark(button_center))
button_center.grid(row=1, column=1)

button_side_right = tkinter.Button(board, text=" ", command=lambda: player_mark(button_side_right))
button_side_right.grid(row=1, column=2)

button_corner_bottomleft = tkinter.Button(board, text=" ", command=lambda: player_mark(button_corner_bottomleft))
button_corner_bottomleft.grid(row=2, column=0)

button_side_bottom = tkinter.Button(board, text=" ", command=lambda: player_mark(button_side_bottom))
button_side_bottom.grid(row=2, column=1)

button_corner_bottomright = tkinter.Button(board, text=" ", command=lambda: player_mark(button_corner_bottomright))
button_corner_bottomright.grid(row=2, column=2)

# If it's currently the AI's turn, the AI immediately makes a move.
if not player_turn:
    ai_mark()

# Enter the main event loop.
board.mainloop()
