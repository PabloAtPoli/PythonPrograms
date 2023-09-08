"""
These are examples from the NLTK book.

"""
# import nltk
# nltk.download()

from nltk.book import text1 # , text2, text3, text4, sent1, sent2, sent3
# import matplotlib.pyplot as plt

# print(text1)
# print(text2)

# print(text1.concordance("monstrous"))
# print(text2.concordance("affection"))
# print(text3.concordance("lived"))

# print("Words that appear in similar contexts as monstrous: ", end="")
# print(text1.similar("monstrous"))

# print("Words that appear in common contexts as monstrous and very: ", end="")
# print(text2.common_contexts(["monstrous", "very"]))

# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])  
# plt.show()


# print("Number of words in text 2 ", len(text3))

# print("Number of unique words in text3: ")
# print(set(text3))
# print("Number of sorted unique words in text3  : ")
# print(sorted(set(text3)))
# print(len(set(text3)))

# print("Generate Text from text3 (The book of Genesis)")
# print(text3.generate())


# print("Lexical richness of text3: ", len(set(text3))/len(text3))

# print("Count of word 'smote' in text3")
# print(text3.count("smote"))
# print("Percentage of word 'a' in text4")
# print(100*text4.count('a')/len(text4))

# def lexical_diversity(text):
#     return len(set(text))/len(text)

# def percentage(count, total):
#     return 100*count/total

# print("Lexical richness of text3: ", lexical_diversity(text3))
# print("Percentage of word 'a' in text4: ", percentage(text4.count('a'), len(text4)))

# sent1 = ['Call', 'me', 'Ishmael', '.']
# print("Length of sent1: ", len(sent1))
# print("Lexical richness of sent1: ", lexical_diversity(sent1))

# print("Sentence 1" , sent1)
# print("Sentence 2" , sent2)
# print("Sentence 3" , sent3) 

# print("Concatenation of sent1 and sent2: ", sent1+sent2)
# print(['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail'])
# print("Append sent2 to sent1: ", sent1.append(sent2))
# print("Append word 'hello' to sent2", sent2.append('hello'))

# print("Word at index 173 in text4")
# print(text4[173])
# print("Index of word 'awaken' in text4")
# print(text4.index('awaken'))

# print("First 10 words in text3")
# print(text3[:10])
# print("Word from index 100 to 200 in text3")
# print(text3[100:200])

saying = ['After', 'all', 'is', 'said', 'and', 'done',
'more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
print(f"The result is {tokens[-2:]}")





