"""
Word Occurrences
Estimate: 30 minutes
Actual:   42 minutes
"""

user_text = input("Enter text you would like to be counted: ")
word_list = user_text.split()  # Split the input text into words
word_dictionary = {}
for word in word_list:
    word = word.strip(".,!?'()[]{}")  # Remove punctuation
    try:
        word_dictionary[word] += 1
    except KeyError:
        word_dictionary[word] = 1

max_length = max(len(word) for word in list(word_dictionary))
for word, count in sorted(word_dictionary.items()):
    print(f"{word:{max_length}} : {count:1}")
