# Food Word Bank Game 

# importing random library
import random
import pandas as pd

# printing a welcome message to the user 
print("Welcome to the FOOD WORD GUESSING GAME! (you'll probably end up hungry lol) ")

# making the food dictionary with categories as keys and specific foods as values 
food_bank = {"Junk" : ("chips", "cookies", "cake", "fries", "soda", "chocolate", "pizza"), 
                "Fruits" : ("apples", "blueberries", "pineapples","oranges", "raspberries", "kiwi", "strawberries"),
                    "Dairy" : ("cheese", "yogurt", "buttermilk", "butter", "cream", "lactose", "whey")}

# want to choose a randomized word from a category. First we need to randomize the keys
categories = list(food_bank.keys())

# test case to see if categories are printed 
# print(categories)

# getting the user's name 
username = input(f"Please enter your username here:  ")


# telling the user what the categories are 
print(f"""Okay, {username}, Here are the categories, each filled with foods to guess: 
      - Junk
      - Fruits
      - Dairy""")

# randomizing the picking of the categories
random_choosing = random.choice(categories)


# we now need to get the specific values out of the keys 
values = food_bank.get(random_choosing)
# randomizing them 
random_category_word = random.choice(values)
# another test case to see if this worked 
# print(random_category_word)

# want to mask the randomly slected word, possibly with a function?

def mask_function(random_category_word, masking_character = "_"):
    """
    This function will take the randomized word
    and mask it with the chosen character to 
    ensure that the word is not revealed to 
    the user 
    """
    word_length = len(random_category_word)
    print(f"The length of your word is {word_length} characters.")
    mask = masking_character * word_length
    return mask 

# import this a module and put into another file 

# # tests
# mask_function("example")
# mask_function("exam")
# mask_function("exam", "$")

masked_word = mask_function(random_category_word)
print(f"AHHH! Your word is from the {random_choosing} category, and here is your word: {masked_word}") 



# empty lists for correct and incorrect guess and word guess turns 
incorrect_letter_bank = []
correct_bank = []
word_guess_turns = 0



while word_guess_turns < 3: 
    letter_guess = input("What is your letter guess for the secret word? Input here: ")

    if letter_guess in random_category_word:
        # count how many times the word appeared 
        right_letter_count = random_category_word.count(letter_guess)
        print(f"Okay smartie! That letter appeared {right_letter_count} times in the secret word!")
        correct_bank.append(letter_guess)
        print(f"correct word bank: {correct_bank}")

        guess_preference = input("Great job! Do you want to try to guess the word? (y/n): ")
        try:
            if guess_preference.lower() not in ["y", "n"]:
                print("Invalid input. Please enter 'y' or 'n'.")
        except ValueError:
            print("try again!!")
            guess_preference = input("Great job! Do you want to try to guess the word? (y/n): ")
        
        if guess_preference.casefold() == "y":
            user_word_guess = input("""Okay! Since you think you're so smart, what is the word? 
                      Input your answer here:  """)
            if user_word_guess.casefold() == random_category_word:
                print("OKAY BIG BRAINNN! YOU GOT IT!")
                break
            else:
                print("That is very wrong lol but good try!")
                word_guess_turns += 1

    else: 
        print("WRONG WRONG WRONG! Try again!! ")
        incorrect_letter_bank.append(letter_guess)
        print(f"Incorrect word bank: {incorrect_letter_bank}")
        word_guess_turns += 1

# combining both correct and incorrect letter guesses to tell the user how many times they guessed 
both_banks = correct_bank + incorrect_letter_bank
scoring = len(both_banks)
print(f"Here is the number of times you guessed: {scoring}")

# making an updated dictionary to store the user's name and their final score
# username and attempts to get the word are the columns 
user_data = {"Username" : username, 
             "Attempts to get the word" : scoring}
user_dataframe = pd.DataFrame([user_data], index=[0])


print(f"Here is the scoreboard for your attempt to guess the word: {user_dataframe}")
print("Hope you had fun!")
exit("Exiting the program... Bye Bye!")


# making a dictionary for username and their score 




# add some improvements: 

# reveal the secret word after the player fails 
# control over how many times the letter is guessed
# more error handling 


# advanced topics 
# make a dictionary for scoring with the players name as the key and the score (using pandas)
# make a dictionary for player name and scores 

# additional points
# 


