"""
These are examples from the NLTK book.

"""
# import nltk
# nltk.download()

from nltk.book import text1
from nltk import FreqDist

saying = ['After', 'all', 'is', 'said', 'and', 'done',
'more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
print(f"The result is {tokens[-2:]}")

# Calculate the frequency distribution of words
fdist1 = FreqDist(text1)

print("The frequency distribution of text Moby Dick")
print(fdist1)
print(f"The type of the frequency of distributions is {type(fdist1)}")

vocabulary1 = list(fdist1.keys())
print(vocabulary1[:50])
print(f"The frequency of the word whale in the book \"Moby Dick\" is {fdist1['whale']}")

print("50 hapaxes in \"Moby Dick\" are the following:")
print(list(fdist1.hapaxes())[:50])


# Get the most common words and their frequencies
most_common_words = fdist1.most_common(50) 

print("The 50 most frequent words in \"Moby Dick\" book are the following")
for word, frequency in most_common_words:
    print(f"{word}: {frequency}")

fdist1.plot(50, cumulative=True)

fdist1.plot(50)









