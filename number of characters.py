# <!-- Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

# Examples of expected behaviour:

# Sample output
# Please type in a word: hey
# There are 3 letters in the word hey
# Thank you!
# Sample output
# Please type in a word: banana
# There are 6 letters in the word banana
# Thank you!
# Sample output
# Please type in a word: b
# Thank you! -->

name = input(' Ente the word that you want the length for : ')
# used to get the input
print(name)
length = len(name) 
#  used to store the actual length
print(f"The word has {length} letters in {name}")
print(" Thank you!")
