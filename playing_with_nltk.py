"""
This script demonstrates NLTK tokenization.

It uses the NLTK library to tokenize the given text into words and sentences.
"""
# nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

TEXT= """
Welcome you to programming knowlege. 
      Lets start with our first tutorial on NLTK. 
      We shall learn the basic of NLTK here
      """
print(word_tokenize(TEXT))
print(sent_tokenize(TEXT))

fdist = FreqDist(word_tokenize(TEXT))
print(fdist)
print(fdist.most_common(3))

fdist.plot(30,cumulative=False)
plt.show()
