import os
import random
import re
import sys

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
    totPage = len(corpus[page])
    prob = {}
    for val in corpus:
        if (val not in prob) and (val != page):
            prob[val] = 1/totPage*damping_factor
        prob[val] += (1-damping_factor)/totPage
    return prob


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    count = {}
    for key in corpus.keys():
        count[key] = 0
    curr = random.choice(list(corpus.keys()))
    count[curr] += 1
    for i in range(n):
        if random.random() < (1-damping_factor):
            curr = random.choice(list(corpus.keys()))
            count[curr] += 1
        elif len(corpus[curr]) > 0:
            curr = random.choice(list(corpus[curr]))
            count[curr] += 1
        else:
            curr = random.choice(list(corpus.keys()))
            count[curr] += 1
    ret = {}
    for key in count.keys():
        ret[key] = count[key]/SAMPLES
        
    return ret
            
            
    
def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    values = {}
    for key in list(corpus.keys()):
        values[key] = 1/len(corpus)
        
    
    
    while True:
        newValues = {}
        diff = []
        for key in values:
            sum = 0
            for j in list(corpus.keys()):
                if len(corpus[j]) == 0:
                    sum += values[j]/len(corpus)
                if key in corpus[j]:
                    sum += values[j]/len(corpus[j])

            newValues[key] = (1-damping_factor)/len(corpus) + damping_factor*sum
            diff.append(abs(values[key]-newValues[key]))
        values = newValues
        if max(diff) < 0.001:
            break
        
    return values


if __name__ == "__main__":
    main()
