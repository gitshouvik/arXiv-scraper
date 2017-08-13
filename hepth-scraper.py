# Scrape new-submissions from arXiv hep-th
#

import sys
import requests
import datetime
import random
import timeit

start = timeit.default_timer()


from bs4 import BeautifulSoup

url = "https://arxiv.org/list/hep-th/new"
r = requests.get(url)

stp = timeit.default_timer() - start
print "[Fetched in ",(round(stp,2)), "s]"

soup = BeautifulSoup(r.content,"html.parser")

# extract part of the webpage that corresponds to new-submissions, cross-lists or replacements
sectors = soup.find_all("dl")

# extract title and author names
title_data = sectors[0].find_all("div", {"class": "list-title mathjax"})
author_data = sectors[0].find_all("div",{"class": "list-authors"})

# print subject line (in bold)
print '\033[1m' + "\n" +str(len(title_data))+" new submissions on hep-th on",datetime.datetime.now().strftime("%d-%m-%Y") + '\033[0m' + '\n'

seq = range(0,len(title_data))
if (str(sys.argv[1])=='r'):
    random.shuffle(seq)


# print seq

for i in range(0,len(title_data)):
    authors = author_data[seq[i]].text.splitlines()
    a_str = ''.join(authors).strip()
    print title_data[seq[i]].text.split(": ",1)[1], a_str.split(":",1)[1].rstrip()
    print ''
