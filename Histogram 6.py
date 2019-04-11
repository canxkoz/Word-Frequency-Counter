import collections
import re
import matplotlib.pyplot as plt

file = open('TEXT.txt', 'r')
file = file.read()
stopwords = set(line.strip() for line in open('TEXT.txt'))
stopwords = stopwords.union(set(['a', 'i', 'mr', 'ms', 'mrs', 'one', 'two', 'said']))
wordcount = collections.defaultdict(int)
""" 
the next paragraph does all the counting and is the main point of difference from the original article.
"""
# \W is regex for characters that are not alphanumerics.
# all non-alphanumerics are replaced with a blank space using re.sub
pattern = r"\W"
for word in file.lower().split():
    word = re.sub(pattern, '', word)
    if word not in stopwords:
        wordcount[word] += 1
# printing most common words
to_print = int(input("How many top words do you wish to print?"))
print(f"The most common words are:")
# the next line sorts the default dict on the values in decreasing  # order and prints the first "to_print".
mc = sorted(wordcount.items(), key=lambda k_v: k_v[1], reverse=True)[:to_print]
# this is continued from the previous assignment
for word, count in mc:
    print(word, ":", count)
# Draw the bart chart
mc = dict(mc)
names = list(mc.keys())
values = list(mc.values())
plt.bar(range(len(mc)),values,tick_label=names)
plt.savefig('bar.png')
plt.show()