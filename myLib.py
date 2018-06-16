#!/usr/bin/python3
import urllib.request

def downloadBook():
    bookUrl = "http://www.gutenberg.org/files/2600/2600-0.txt"
    url = (bookUrl)
    print ("downloading the book...")
    urllib.request.urlretrieve(url, 'book.txt')

def dummy():
    print ("lala")
