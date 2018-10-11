#!/usr/bin/python
 # -*- coding: utf-8 -*-

from rake_nltk import Rake
import operator


r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

sample_file = open("sonic.txt", 'r')
text = sample_file.read()
keywords = r.extract_keywords_from_text(text)
phrases = r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
count = 0
for key in phrases:
	if count < 50:
		print("<li>"+key+"</li>")
	else:
		pass
	count = count+1
