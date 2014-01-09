#!/usr/bin/env python
# -*- coding: utf_8 -*-
from __future__ import print_function
import os
import sys
import amazonproduct.errors
from amazonproduct import API
import argparse
import csv
import re
import codecs
import time
import random
import urllib2
import socket
import logging
from Queue import Queue
from threading import Thread

logging.basicConfig(format='%(message)s',
					filename = 'test.tsv',
					level = logging.INFO)

def load_csv_file (path):
	r"""
	:result: list<string> string is isbn
	"""

	if os.path.exists(path) == False:
		raise Exception("Not Found Path")

	buff = []
	for row in csv.reader(file(path)):
		if row[0] == "Date":
			continue
		buff.append(row[3])
	return buff

def profile(func):
	def wrap(*args, **kwargs):
		started_at = time.time()
		result = func(*args, **kwargs)
		print("Performance: {0}".format(time.time() - started_at))
		return result

	return wrap

def request_amzn (isbn):
	r"""
	Get The Book Title and asin code from Amazon.

	:param isbn: ISBN string
	:return: tuple (Book titile, Asin Code, XML RootNode)
	"""

	api = API(locale='jp')
	root = api.item_lookup(isbn,SearchIndex='Books', IdType='ISBN')

	root = api.item_lookup(isbn,SearchIndex='Books', IdType='ISBN')
	book = root.xpath(
		"//aws:Items/aws:Item/aws:ItemAttributes/aws:Title",
		namespaces={"aws": root.nsmap.get(None, '')}
	)
	asin = root.xpath(
		"//aws:Items/aws:Item/aws:ASIN",
		namespaces={"aws": root.nsmap.get(None, '')}
	)
	return (book, asin, root)


@profile
def request_amazon(isbn_list):
	r"""
	Requested Amazon.
	"""
	counter = 0
	while not isbn_list.empty():
		isbn = isbn_list.get()
		print("I Run {0}".format(isbn))
		start = time.time()
		book = asin = root = None
		
		while True:
			try:
				(book, asin, root) = request_amzn(isbn)
				break
			except amazonproduct.errors.TooManyRequests, e:
				wait_sec = random.randint(10*1, 10*5)
				print("Too Many Requests... waiting {0}sec".format(wait_sec))
				time.sleep(wait_sec)

			except urllib2.URLError, e:
				wait_sec = random.randint(10*1, 10*5)
				print("URLLib error Requests... waiting {0}sec".format(wait_sec))
				time.sleep(wait_sec)

			except socket.error, e:
				wait_sec = random.randint(10*1, 10*5)
				print("socket.error error Requests... waiting {0}sec".format(wait_sec))
				time.sleep(wait_sec)

			except socket.timeout, e:
				wait_sec = random.randint(10*1, 10*5)
				print("socket.error error Requests... waiting {0}sec".format(wait_sec))
				time.sleep(wait_sec)

			except urllib2.HTTPError, e:
				wait_sec = random.randint(10*1, 10*5)
				print("HTTPError error Requests... waiting {0}sec".format(wait_sec))
				time.sleep(wait_sec)

			except Exception, e:
				print("erro except {0}...".format(str(e)))
				break


		if book:
			counter += 1
			book = book[0].text
			asin = unicode(asin[0].text, "utf8")
			isbn = unicode(isbn, "utf8")
			end = time.time()
	
			print("[{2} sec]{0}/{1}".format(counter, isbn_list.qsize(), end-start), end="\n")
			logging.info(u"{0}\thttp://www.amazon.co.jp/dp/{1}\t{2}".format(book, asin, isbn))
		else:
			from lxml import etree
			print(etree.tostring(root, pretty_print=True), file=sys.stderr)

		time.sleep(random.randint(1,5))
	isbn_list.task_done()
	# print "Result: %s" % (root.Items.Item)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Get Book Title in csv file. title get from aws.')
	parser.add_argument('csv', metavar='c', type=str, nargs='?', default="", help='Read CSV File')
	args = parser.parse_args()

	num_fetch_threads = 4
	isbns = load_csv_file(args.csv)
	isbn_queue = Queue()

	for i in range(num_fetch_threads):
		worker = Thread(target=request_amazon, args=(isbn_queue,))
		worker.setDaemon(True)
		worker.start()

	for isbn in isbns:
		isbn_queue.put(isbn)
	print("Queue:{0}".format(isbn_queue))

	isbn_queue.join()
	print("done")


