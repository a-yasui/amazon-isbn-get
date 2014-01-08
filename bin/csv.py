#!/usr/bin/env python
import os
import sys
from amazonproduct import API
import argparse
import csv
import re


def load_csv_file (path):
	r"""
	:result: list<string> string is isbn
	"""

	if os.path.exists(path) == False:
		raise Exception("Not Found Path")

	buff = []
	for row in csv.reader(open(path, 'rb')):
		if row[0] == "Date":
			continue
		buff.append(row[3])
	return buff

parser = argparse.ArgumentParser(description='Get Book Title in csv file. title get from aws.')
parser.add_argument('--csv', metavar='c', type=str, nargs='?', default=None, help='Read CSV File')

api = API(locale='jp')
root = api.item_lookup('9784840238793', IdType='ISBN',
            SearchIndex='Books', ResponseGroup='Reviews', ReviewPage=1)
print root


