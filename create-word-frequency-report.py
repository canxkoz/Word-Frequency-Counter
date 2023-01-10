from collections import Counter
import numpy as np
import re
import chardet
import matplotlib as mpl
import sys
mpl.use('MacOSX') # optional (depends on user's operating system)
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']
import matplotlib.pyplot as plt
import argparse

def openfile(Filename):
    with open(Filename, 'rb') as f:
        result = chardet.detect(f.read())
        f.seek(0)
        txt = f.read().decode(result['encoding'])
    return txt

def removegarbage(str):
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str

def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt

def plot_histogram(nums,labels,Filename=None):
    plt.figure(1,figsize=(16,8))
    bins = np.arange(0,len(labels))
    bar_width = 0.8*(bins[1]-bins[0])
    plt.bar(bins,nums,bar_width)
    plt.xticks(bins,labels,rotation=90, ha='center',fontsize=9)
    if Filename is not None:
        plt.title(f'Word Frequency Report for {Filename}')
    else:
        plt.title('Word Frequency Report')
    plt.tight_layout()
    plt.show(block=True)
    
def main():
    parser = argparse.ArgumentParser(description='Plot a histogram of the top N most common words in a text file.')
    parser.add_argument('Filename', type=str, help='Path to the text file')
    parser.add_argument('topwords', type=int, help='The number of most common words to be plotted')
    args = parser.parse_args()
    Filename = args.Filename
    topwords = args.topwords
    # rest of the code
    txt = openfile(Filename)
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    nums = []
    labels = []
    for key, value in bins.most_common(topwords):
        if key not in ['we','our','they','i','mr','ms','mrs','one','two','said','also','have','from','the','of','are','and','in','to','for','a','will','be','on','with','is','1','2','3','4','5','6','7','8','9','by','this','at','as','we','can','has','that','an','which','or'] and len(key) > 1:
            nums.append(value)
            labels.append(key)
    plot_histogram(nums,labels,Filename)

if __name__ == "__main__":
    sys.exit(main())