from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

word_list = ['A', 'A', 'B', 'B', 'A', 'C', 'C', 'C', 'C']

counts = Counter(word_list)

labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.35

plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.show()