import re
import math
import numpy as np
from typing import List


def domain_name(url):
    url = url.replace('www.', '')
    return re.findall('[^a-z]+(.+?)\.', url)[0] if url.startswith('http') else url.split('.')[0]

def solution(number):
    if number < 0:
        return 0
    else:
        nlist = [x + 1 for x in range(number - 1) if ((x+1) % 3) == 0 or ((x+1) % 5) == 0]
        return sum(nlist)

def rgb(r, g, b):
    int = (r if r < 256 and r >= 0 else (255 if r > 255 else (0 if r < 0 else '')),g if g < 256 and g >= 0 else (255 if g > 255 else (0 if g < 0 else '')),b if b < 256 and b >= 0 else (255 if b > 255 else (0 if b < 0 else '')))
    return '%02x%02x%02x'.upper() % int

def pig_it(text):
    return ' '.join([x[1:] + x[0] + 'ay' if re.search('[a-z]+',x.lower()) else x for x in text.split(' ') ])


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.items = len(collection)
        self.pages = math.ceil(len(collection) / items_per_page)
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return self.items
    # returns the number of pages
    def page_count(self):
        return self.pages
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        nitems = self.items
        itemsPerPage = dict()
        x = 0
        for page in range(self.pages):
            if nitems <= self.items_per_page:
                itemsPerPage[page] = nitems
            else:
                itemsPerPage[page] = self.items_per_page
                nitems = nitems - self.items_per_page

        try:
            return itemsPerPage[page_index]
        except:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or self.items == 0:
            return -1
        item_index = item_index + 1
        if item_index > self.items:
            return -1
        else:
            return math.ceil(item_index / self.items_per_page) - 1

collection = range(1,25)
helper = PaginationHelper(collection, 10)
#print(helper.page_count())
#print(helper.page_index(23))
#print(helper.item_count())

def dbl_linear(n):
    arr = np.array([1])
    pos = 0
    while n > pos:
        arr = np.append(arr,(arr[pos] * 2) + 1)
        arr = np.append(arr,(arr[pos] * 3) + 1)
        arr = np.sort(arr)
        pos += 1
    arr = np.unique(arr)
    return arr[n]

print(dbl_linear(20))
#print(max_sequence([24, -4, -29, 8, -24, 6, 3, 0, 21, -21, 14, -6, -19, 14, -25, -5, 12, -11, -25, 5, 12, 7, 23, 8, -13, 13, -10, -4, 6, 0, 1, 12, -9, -25, 2, 22, 30, 0, 13, 13, -1, 30, 19, -8, -6, 9, 26, -6, 23, -23]))
# print(pig_it('O tempora o mores !'))