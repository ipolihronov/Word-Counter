#!/usr/bin/python3

def downloadBook():
    url = (bookUrl)
    print ("downloading the book...")
    urllib.request.urlretrieve(url, 'book.txt')

def dummy():
    print ("lala")
