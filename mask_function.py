
def mask_function(random_category_word, masking_character = "*"):
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