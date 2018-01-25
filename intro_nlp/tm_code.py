import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
from bs4 import BeautifulSoup

file = "html/article1.html"
print(open(file, "r").readlines())

from bs4 import BeautifulSoup

with open(file, "r") as f:
  soup = BeautifulSoup(f, "html.parser")

  for div in soup.find_all("div", id="article-body"):
    for p in div.find_all("p"):
      print(p.get_text())


from __future__ import unicode_literals
import unicodedata