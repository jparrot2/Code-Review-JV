# Food Word Bank Game 

# importing random library
import random

# printing a welcome message to the user 
print("Welcome to the FOOD WORD GUESSING GAME! (you'll probably end up hungry lol) ")

# making the food dictionary with categories as keys and specific foods as values 
food_bank = {"Junk" : ("chips", "cookies", "cake", "fries", "soda"), 
                "Fruits" : ("apples", "blueberries", "pineapples","oranges", "raspberries"),
                    "Dairy" : ("cheese", "yogurt", "buttermilk", "butter", "cream")}

# want to choose a randomized word from a category. First we need to randomize the keys
categories = list(food_bank.keys())

# test case to see if categories are printed 
# print(categories)

# telling the user what the categories are 
print("""Here are the categories, each filled with words to guess: 
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
def mask_function(random_category_word, masking_character = "#"): 
    word_length = len(random_category_word)
    print(f"The length of your word is {word_length} characters.")
    mask = masking_character * word_length
    return mask 

masked_word = mask_function(random_category_word)
print(f"AHHH! Your word is from the {random_choosing} category, and here is your word: {masked_word}") 



# empty lists for correct and incorrect guess and word guess turns 
incorrect_letter_bank = []
correct_bank = []
word_guess_turns = 0



while True: 
    letter_guess = input("What is your letter guess for the secret word? Input here: ")

    if letter_guess in random_category_word:
        # count how many times the word appeared 
        right_letter_count = random_category_word.count(letter_guess)
        print(f"Okay smartie! That letter appeared {right_letter_count} times in the secret word!")
        correct_bank.append(letter_guess)
        print(f"correct word bank: {correct_bank}")
        guess_preference = input("Great job! Do you want to try to guess the word? (y/n): ")
        if guess_preference.lower() not in ["y", "n"]:
            raise ValueError("Invalid input. Please enter 'y' or 'n'.")
        if guess_preference.casefold() == "y":
            user_word_guess = input("""Okay! Since you think you're so smart, what is the word? 
                      Input your answer here:  """)
            if user_word_guess.casefold() == random_category_word:
                print("OKAY BIG BRAINNN! YOU GOT IT!")
            else:
                print("That is very wrong lol but good try!")
                word_guess_turns += 1

    else: 
        print("WRONG WRONG WRONG! Try again!! ")
        incorrect_letter_bank.append(letter_guess)
        print(f"Incorrect word bank: {incorrect_letter_bank}")
