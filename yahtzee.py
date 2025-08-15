"""
Description:
  An implementation of the dice game "Yahtzee" in Python with some changes.
"""
import random

TOTAL_DICE = 5
DICE_FACES = 6
FULL_HOUSE = 25
SMALL_STRAIGHT = 30
LARGE_STRAIGHT = 40
PYTZEE = 50

score_board = {"1's":0, "2's":0, "3's":0, "4's":0, "5's":0, "6's":0, "Three of a Kind" :0, 
                 "Four of a Kind":0, "Full House": 0,"Small Straight":0, "Large Straight":0, 
                 "Pytzee":0, "Chance": 0} #The official scoreboard in the form of a dictionary

corresponding_dict = {"count 1": "1's", "count 2": "2's", "count 3": "3's", "count 4": "4's", "count 5": "5's", "count 6": "6's",
                      "full house": "Full House", "small straight": "Small Straight", "large straight": "Large Straight",
                      "three of a kind": "Three of a Kind", "3 of a kind": "Three of a Kind", "four of a kind":"Four of a Kind",
                       "4 of a kind": "Four of a Kind", "pytzee":"Pytzee", "chance":"Chance"} # This will correspond the user input to the board's key, which are used to update the values. 

def roll_dice():
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    return roll_list

def count_dice(dice_lst, number): #Counts the instances of a specific number, the number being user's choice
    return dice_lst.count(number)

def display_board(board):
    for key, value in board.items(): #Displays the board in a vertical manner
        print(f"|{key} : {value}|\n")

def check_if_category_taken(add_to): #Checks if the category that the user wants to add to is already occupied or not
    flag = True
    while flag:
        if score_board[corresponding_dict[add_to]] != 0:
            add_to = input("This category is already taken. Please select another category. ") #If the category is taken (not 0), it prompts accordingly.
        else:
            flag = False
    return add_to

def update_and_display_score(board): #updates the board's "value" part to the total
    total = 0
    for value in board.values():
        total += value
    return total

def singles(dice_lst, add_to): #Accounts for every upper section input (count 1 - count 6). 
    add_to = check_if_category_taken(add_to) #First, we must check if the category is not taken. If this equals True, the user is prompted to select another category.
    number = int(add_to[6])
    score_value = count_dice(dice_lst, number) * number
    score_board[corresponding_dict[add_to]] = score_value #Associating the user input to the key value of the scoreboard
    print(f"Accepted the {number}")

def three_of_a_kind(dice_lst, add_to): #The algorithm to account for a three-of-a-kind.
    add_to = check_if_category_taken(add_to)
    score_value = 0
    for i in range(1, 7):
        if dice_lst.count(i) == 3: #Checks if the number occurs 3 times in the list.
            score_value = sum(dice_lst)
    
    score_board[corresponding_dict[add_to]] = score_value
    print("Three of a Kind!")

def four_of_a_kind(dice_lst, add_to): #Algorithm to account for a four-of-a-kind.
    add_to = check_if_category_taken(add_to)
    score_value = 0
    for i in range(1, 7):
        if dice_lst.count(i) == 4: #Checks if the number occurs 4 times in the list
            score_value = sum(dice_lst)
    
    score_board[corresponding_dict[add_to]] = score_value
    print("Four of a Kind!")

def full_house(dice_lst, add_to): #Algorithm to account for a full house
    add_to = check_if_category_taken(add_to)
    score_value = 0
    for num in dice_lst:
        if dice_lst.count(num) == 3: #if any 1 number occurs 3 times in the dice roll
            for another_num in dice_lst:
                if another_num != num: #Select another number except the number that occured 3 times previously
                    if dice_lst.count(another_num) == 2: #If that number occurs the remaining 2 times, then full house is activated.
                        score_value = FULL_HOUSE
    
    score_board[corresponding_dict[add_to]] = score_value
    print(f"You have a full house and get {FULL_HOUSE} points.")

def small_straight(dice_lst, add_to): #Algorithm to account for a small straight
    add_to = check_if_category_taken(add_to)
    score_value = 0
    dice_lst.sort() #Sort the dice

    new_dice_lst = []
    for x in dice_lst: 
        if x not in new_dice_lst: #Getting rid of duplicates
            new_dice_lst.append(x)

    for i in range(len(new_dice_lst) - 3):
        if [1, 2, 3, 4] == new_dice_lst[i:i+4] or [2, 3, 4, 5] == new_dice_lst[i:i+4] or [3, 4, 5, 6] == new_dice_lst[i:i+4]: #One of these lists are the combination that must be achieved for a small straight
            score_value = SMALL_STRAIGHT
    
    score_board[corresponding_dict[add_to]] = score_value
    print(f"You have a small straight and get {SMALL_STRAIGHT} points.")

def large_straight(dice_lst, add_to): #Algorithm to account for a large straight
    add_to = check_if_category_taken(add_to)
    score_value = 0
    dice_lst.sort() #Sort the dice 

    new_dice_lst = []
    for x in dice_lst:
        if x not in new_dice_lst: #Getting rid of duplicates
            new_dice_lst.append(x) 
    
    for i in range(len(new_dice_lst)):
        if new_dice_lst[i:i+5] == [1, 2, 3, 4, 5] or new_dice_lst[i:i+5] == [2, 3, 4, 5, 6]: #One of these lists are the combination that must be achieved for a large straight
            score_value = LARGE_STRAIGHT
    
    score_board[corresponding_dict[add_to]] = score_value
    print(f"You have a large straight and get {LARGE_STRAIGHT} points.")

def pytzee(dice_lst, add_to): #Algorithm to account for a pytzee
    score_value = 0
    if score_board["Pytzee"] == 0:
        for num in dice_lst:
            if dice_lst.count(num) == 5: #All dice must be the same roll
                score_value = PYTZEE
        print(f"You have a pytzee and get {PYTZEE} points.")
    else:
        score_value = 100
        print(f"You have an additional pytzee and get 100 points.")

    score_board[corresponding_dict[add_to]] += score_value

def chance(dice_lst, add_to): #Algorithm to account for a chance
    add_to = check_if_category_taken(add_to)
    score_value = 0

    for num in dice_lst:
        score_value += num
    
    score_board[corresponding_dict[add_to]] = score_value
    print(f"You have chance and get {score_value} points.")

def play_game(num_rounds): #The main game function that arranges the magic
    for i in range(1, num_rounds + 1):
        dice_roll = roll_dice() #Use the dice roll as a parameter fo the functions that execute as follows.
        print(f"***** Beginning round {i} *****")
        print(f"Your score is: {update_and_display_score(score_board)}")
        print(dice_roll)
        count_to = input("How would you like to count this roll? ").lower()
        
        flag2 = True
        while flag2:
            if count_to in corresponding_dict or count_to == "skip":
                flag2 = False
            else:
                count_to = input("How would you like to count this roll? ").lower()
        #Using the user's input to execute the proper algorithm
        if count_to[:5] == "count":
            singles(dice_roll, count_to)
        elif count_to == "skip": #The skip algorithm: We add to the current round, display the score, roll a new dice and let the loop re-run.
            print(f"***** Beginning round {i + 1} *****")
            print(f"Your score is: {update_and_display_score(score_board)}")
            print(dice_roll)
        elif count_to == "three of a kind" or count_to == "3 of a kind":
            three_of_a_kind(dice_roll, "three of a kind")
        elif count_to == "four of a kind" or count_to == "4 of a kind":
            four_of_a_kind(dice_roll, "four of a kind")
        elif count_to == "full house":
            full_house(dice_roll, count_to)
        elif count_to == "small straight":
            small_straight(dice_roll, count_to)
        elif count_to == "large straight":
            large_straight(dice_roll, count_to)
        elif count_to == "pytzee":
            pytzee(dice_roll, count_to)
        elif count_to == "chance":
            chance(dice_roll, count_to)

        display_board(score_board)
    total_score = update_and_display_score(score_board)

    if score_board["1's"] + score_board["2's"] + score_board["3's"] + score_board["4's"] + score_board["5's"] + score_board["6's"] >= 63:
        total_score += 35 #If the upper section's values summed are greater than 63, we add the bonus.

    print(f"Your final score is: {total_score}") #Displaying the final score after all rounds have concluded.

if __name__ == '__main__': #Execution of the magic
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)
