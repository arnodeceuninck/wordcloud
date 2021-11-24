"""
Creates a wordcloud from the most frequently occuring words in a pdf file
"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from tika import parser
from pprint import pprint

def main():
    with open('input.txt', 'r') as file:
        text = file.read().replace('\n', ' ')

    raw = parser.from_file('input.pdf')
    text = raw['content']

    with open('stopwoorden.txt') as f:
        stopwords = f.read().splitlines(keepends=False)

    word_cloud = WordCloud(collocations=False, background_color='white', stopwords=stopwords).generate(text)

    words_sorted = sorted(word_cloud.words_.items(), key=lambda word: word[1])
    pprint(words_sorted)

    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
