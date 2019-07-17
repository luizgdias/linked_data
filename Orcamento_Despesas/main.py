# -*- coding: utf-8 -*-

import csv, os, sys, codecs 
import unicodedata as ud

def list_categories():
	os.system('touch categories.txt')
	categories = open('categories.txt', 'a')
	with open('data/2019_OrcamentoDespes.csv', 'r') as file:
		reader = csv.reader(file)
		i = reader.next()
		rest = [row for row in reader]
		cat = (str(i))
		cat.encode('utf8')
		print(cat)
		categories.write(str(cat))

	categories.close()


list_categories()