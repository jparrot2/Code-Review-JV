# beginning data analysis examples 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# importing numpy as the name np (easier way to use it as a module)
# this is called an alias?

# does computation with numbers and data analysis applications

# ARRAYS 
# CAN ONLY BE ONE TYPE OF THING (only numbers for example)

# lets make a list 
number_list = [1, 2, 22, 89]
string_list = ["a", "c", "something", "else"]

# you can mix numbers and strings in a list 
mixed_list = [1, "c", 22, "something"]

number_array = np.array(number_list)
# taking number list and putting it as an array
print(number_array)
type(number_array) # wil
number_array.dtype #dtype tells you specifically what stuff is in the array

# now what if you try to make a mixed list an array?
mixed_array = np.array(mixed_list)
print(mixed_array)
# just puts all of the contents as a string 

# make a dictionary to hold some data 
# great because it gives key value pairs 

fruit_dictionary = {"apples" : 3.49, 
                "bananas" : 1.79,
                "strawberries" : 5.99}

# we can get the specifc values this way: kind of like indexing?
# giving it the key and we can get back the value 
fruit_dictionary["bananas"]

# how to just grab the values from the dictionary
# dictionary name . values and list to turn the values 
# to a list 
fruit_prices = list(fruit_dictionary.values())
print(fruit_prices)

fruit_tax = 0.1 #10% fruit tax,how do we apply this to the values 
taxed_prices = []
# use a for loop to apply!

for price in fruit_prices:
    taxed_price = price * (1 + fruit_tax)
    taxed_price = round(taxed_price, 2) # rounding to 2 decimal places 
    taxed_prices.append(taxed_price)
print(taxed_prices)







#LIST COMPREHENSION 
# cramming everything in one line
#FORMAT: the loop at the end and what you want it to do in FRONT
taxed_prices_2 = [round(price * (1 + fruit_tax), 2) for price in fruit_prices]
print(taxed_prices_2)



# EASIER WAY TO DO THIS (WITHOUT LOOPS) = USE AN ARRAY!
# does this to each thing in the array
taxed_prices3 = np.array(fruit_prices) * (1 + fruit_tax)
print(taxed_prices3)
taxed_prices3 = taxed_prices3.round(2) # EASIER WAY TO ROUND!
print(taxed_prices3)


# arange 
range(10)
print(np.arange(10)) # gives us numbers from 0 to 9
print(np.arange(3, 9))
print(np.arange(3, 28, 3))




############################################################
# DATA FRAMES AND USING PANDAS 

# what is a dataframe?
# like an excel spreadsheet
# each column is at variable rows are different observations

# we can go from dictionaries to dataframes 
# we have to make some changes to the dictionary to make 
# appropriate names for the columns (ie fruit names and prices)

# how to get the keys: 
# call the dictionary, get the keys, and turn into a list
fruit_names = list(fruit_dictionary.keys())

# making a more formatted dictionary
fruit_data = {"fruit" : fruit_names, 
              "prices" : fruit_prices}
print(fruit_data)

fruit_dataframe = pd.DataFrame(data = fruit_data)
print(fruit_dataframe) # IT IS NOW IN A DATAFRAME!

# doing things with the dataframe:
fruit_dataframe.describe() #gives stuff about the data (mean, SD, etc)
fruit_dataframe["prices"].mean() # we can get the average price
fruit_dataframe["prices"].dtype