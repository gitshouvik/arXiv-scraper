# arXiv scraper

This is a scraper for listing the new submissions from [arxiv/hep-th](https://arxiv.org/list/hep-th/new) made using BeautifulSoup. It lists the titles and authors of the articles.

To list them in a random order use :
```sh
$ python hepth-scraper.py r
```
To list them in a original order as on the webpage use :
```sh
$ python hepth-scraper.py n
```

The subject class used here is hep-th, which can be changed easily in the program. 

