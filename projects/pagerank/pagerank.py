import os
import random
import re
import sys
import numpy as np
import pandas as pd
from collections import Counter

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    model = {}
    for i in corpus:
        model[i] = 0
        model[i] += (1 - damping_factor)/len(corpus)
        for link in corpus[page]:
            if link == i:
                model[i] += damping_factor/len(corpus[page])
    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    samples = []
    page = random.choice(list(corpus))
    for i in range(n):
        model = transition_model(corpus, page, damping_factor)
        new_page = random.choices(list(corpus), list(model.values()))[0]
        samples.append(new_page)
        page = new_page

    chain = Counter(samples)
    chain = dict(chain)

    chain = dict(map(lambda item: (item[0], item[1]/n), chain.items()))
    
    chain = dict(sorted(chain.items(), key=lambda item: item[1], reverse=True))

    return chain



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ranks = {}
    N = len(corpus)
    for page, links in corpus.items():
        last_rank = 0
        rank = (1-damping_factor)/N
        while abs(last_rank - rank) >= 0.001:
            last_rank = rank
            rank = (rank/len(links))*damping_factor

        ranks[page] = rank

    total = sum(ranks.values())
    for page in ranks:
        ranks[page] /= total
        

    return ranks


if __name__ == "__main__":
    main()
