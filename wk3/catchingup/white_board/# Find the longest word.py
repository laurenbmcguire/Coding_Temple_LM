# Find the longest word
# Create a function that given a string as a parameter of space-separated words
# find and return the word with the most characters
# Input
a1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
# Output
# consectetur
def longest_word(a_str):
    longest_word =''
    words=[]
    for word in a_str.split():
        if len(word) > len(longest_word):
            longest_word=word
    return longest_word
print(longest_word(a1))