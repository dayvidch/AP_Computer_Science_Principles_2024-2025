# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
# def one_word(password):
#   words = get_dictionary()
#   guesses = 0
#   # get each word from the dictionary file
#   for w1 in words:
#     for w2 in words:
#       guesses += 1
#       w = w1 + w2
#     if (w == password):
#       return True, guesses
#   return False, guesses

def one_word(password):
    words = get_dictionary()
    digits = "0123456789"  # Define a string of digits
    guesses = 0
    
    # Get each word from the dictionary file
    for w1 in words:
        for w2 in words:
            # Concatenate the words to check for the combined password
            phrase = w1 + w2

            # Iterate through digits and prepend and append each digit
            for digit in digits:
                # Prepend digit
                guess = digit + phrase
                guesses += 1
                if guess == password:
                    return True, guesses

                # Append digit
                guess = phrase + digit
                guesses += 1
                if guess == password:
                    return True, guesses

    return False, guesses
