import nltk
import re
import os
import dill
from collections import OrderedDict

import ip_handling

def nltk_download_packages():
    nltk.download("words")
    nltk.download("brown")
    nltk.download("abc")
    nltk.download("inaugural")
    nltk.download("genesis")

def get_words_from_nltk():
    def _g_lim():
        w_lower_lim = 2
        w_upper_lim = 12
        g_lim = lambda w: len(w) > w_lower_lim and len(w) < w_upper_lim
        return g_lim
    
    g_lim = _g_lim()
    a_words = lambda ws, tx:  ws + [w.lower() for w in tx if g_lim(w)]
    
    def _nltk():
        words = a_words([], nltk.corpus.words.words())
        words = a_words(words, nltk.corpus.brown.words())
        words = a_words(words, nltk.corpus.abc.words())
        words = a_words(words, nltk.corpus.inaugural.words())
        words = a_words(words, nltk.corpus.genesis.words('english-kjv.txt'))
        words = a_words(words, nltk.corpus.genesis.words('english-web.txt'))
        return words
    
    try:
        words = _nltk()
    except:
        nltk_download_packages()
        words = _nltk()

    reg = re.compile("^([a-z]+)+$")
    words = [w for w in words if bool(reg.match(w))]

    return words

def load_words(num_words):
    
    words = get_words_from_nltk()
    fdist = nltk.FreqDist(words)

    fdistmc = fdist.most_common()

    nd = OrderedDict()
    nda = []

    occurences = set([wt[1] for wt in fdistmc])
    occurences = sorted(occurences, key=int, reverse=True)

    for idx in occurences:
        nd[idx] = sorted([wt[0] for wt in fdistmc if wt[1] == idx])
    
    for key, val in nd.items():
        nda += val
    
    words = nda[:num_words]
    return words

def dill_words(num_words, fname="words.dill"):
    try:
        if os.path.isfile(fname):
            words = dill.load(open(fname, "rb"))
            if(len(words) < ip_handling.get_ipv6_word_possibilities()):
                os.remove(fname)
                raise Exception # go into except block to reload words
            return words
        else:
            words = load_words(num_words)
            if(len(words) < ip_handling.get_ipv6_word_possibilities()):
                raise Exception # go into except block to reload words
            dill.dump(words, open(fname, "wb"))
            return words
    except:
        try:
            words = load_words(num_words)
            if(len(words) < ip_handling.get_ipv6_word_possibilities()):
                raise Exception # go into except block to reload words
            dill.dump(words, open(fname, "wb"))
            return words
        except:
            return load_words(num_words)