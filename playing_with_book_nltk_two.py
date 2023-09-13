"""
These are examples from the NLTK book.

"""
# import nltk
# nltk.download()

from nltk.book import text1, text4, text5
from nltk import FreqDist, bigrams

# saying = ['After', 'all', 'is', 'said', 'and', 'done',
#           'more', 'is', 'said', 'than', 'done']
# tokens = set(saying)
# tokens = sorted(tokens)
# print(f"The result is {tokens[-2:]}")

# Calculate the frequency distribution of words
fdist1 = FreqDist(text1)

print("The frequency distribution of text Moby Dick")
print(fdist1)
print(f"The type of the frequency of distributions is {type(fdist1)}")

# Find frequency of distribution in descending order
vocabulary1 = list(fdist1.keys())
print("The 50 most frequent tokens in the 'Moby Dick' book are the following: ")
print(vocabulary1[:50])
print()

print(
    f"The frequency of the word whale in the book \"Moby Dick\" is {fdist1['whale']}")

print("50 hapaxes in \"Moby Dick\" are the following:")
print(list(fdist1.hapaxes())[:50])
print()


# # Get the most common words and their frequencies
most_common_words = fdist1.most_common(50)

print("The 50 most frequent words in \"Moby Dick\" book are the following")
for word, frequency in most_common_words:
    print(f"{word}: {frequency}")

# Show the cumulative frequency graph for the text Moby Dick
fdist1.plot(50, cumulative=True)

# Show the cumulative frequency graph for the text Moby Dick
fdist1.plot(50)

# # List the words in text1 whose length is greater than 15
# V = set(text1)
# long_words = [w for w in V if len(w) > 15]
# sorted(long_words)
# print("The words in text Moby Dick whose length are greater than 15 are the following:")
# print(sorted(long_words))
# print()


# # Words in the Corpus chat that are longer than 7 characters
# fdist2 = FreqDist(text5)
# print("Words in the Corpus chat that are longer than 7 characters and their frequency is greater than 7:")
# print(sorted([w for w in set(text5) if len(w) > 7 and fdist2[w] > 7]))
# print()


# # Extracting biagrams from a list of words
# print(
#     "The bigrams from the list ['more', 'is', 'said', 'than', 'than'] are the following")
# print(list(bigrams(['more', 'is', 'said', 'than', 'than'])))
# print()

# # Collocation of text4
# print("The collocation of text4, Inaugural Address Corpus, are the following:")
# print(text4.collocations())
