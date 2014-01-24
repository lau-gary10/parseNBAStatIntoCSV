'''
import tkinter
from tkinter import ttk
from urllib.request import urlopen


def download(event):
    file = urlopen('http://stats.nba.com/js/data/sportvu/speedData.js')
    output = open('C:/Users/glau/Downloads/nbaSpreadsheets/downloaded_file.txt', 'wb')

'''

# Reads data in chunks
import urllib.request

urlFile = urllib.request.urlopen("http://stats.nba.com/js/data/sportvu/speedData.js")

data_list = []
chunk = 4096
while 1:
    data = urlFile.read(chunk)
    if not data:
        print("done.")
        break
    data_list.append(data)
    print("Read %s bytes"%len(data))