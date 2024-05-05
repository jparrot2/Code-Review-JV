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
letter_guess = input("OOOOKAY, what is your letter guess? Input here:  ")