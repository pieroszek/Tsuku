#!/usr/bin/env python3
import argparse
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

data_file_path = os.path.join(script_dir, 'data.txt')


Args = []
Items = ["empty"]

createVar = "c"
remVar = "r"
listVar = "l"


def getFile():
    data = ""
    try: 
        with open(data_file_path, 'r') as file :
            data = file.readline()
            data.strip()
            return data
    except FileExistsError or FileNotFoundError :
        print("no data file, created one")
        with open(data_file_path, 'x') as file:
            data = file.readlines()
            return data

def readFile(data):

    try:
    #if True:
        Items.clear()
        i = 0
        item = ""
        while i < len(data):
            if data[i] != '|':
                item = item + data[i]
            elif data[i] == '|':
                Items.append(item)
                item = ""
            i = i + 1
    except:
       print("parser brok")

def clearFile():
    try:
        with open(data_file_path, 'w') as file:
            pass
    except:
        print("ckear file brok")


def writeFile():
    strnToAdd = ""    
    try:
        with open(data_file_path,'w') as file:
            for x in Items:
                strnToAdd = strnToAdd + x + '|'
            file.write(strnToAdd)
    except FileExistsError:
        print("file no existe")
    except:
        print("write error")

####
def parseArgs():
    i = 0
    for x in sys.argv:
        if i > 0:
            #print(x)
            Args.append(x)
        i = i + 1



def showItems():
    index = 0
    for item in Items:
        print(index, "- ", item)
        index = index + 1 


def showArgs():
    for arg in Args:
        print(arg)

def create():
    newItem = ""   
    if Args[0] == createVar:
        if len(Args) > 2:
            i = 1
            for i in range (1,len(Args)):
                if i == 1:
                    newItem = Args[1]
                else:
                    newItem = newItem + " " + Args[i]
        else:
            newItem = Args[1]
        Items.append(newItem)

        

def remove():
    print("**curr List**")
    showItems()
    if len(Args) == 1:
        delItem = input("rem item: ")
        i = 0
        for x in Items:
            if x == delItem or str(i) == delItem:
                Items.remove(x)
                break
            i = i + 1
    elif Args[0] == remVar:
        for x in Items:
            if x == Args[1]:
                Items.remove(x)



def list():
    print("**List**")
    data = getFile()
    readFile(data)
    showItems()
        

def argsToItems():

    for arg in Args:
        Items.append(arg)

def main():
    print(getFile())
    parseArgs()
    match Args[0] :
        case "c":
            data = getFile()
            clearFile()
            readFile(data)
            create()
            writeFile()
            showItems()
            Items.clear()
        case "r":
            data = getFile()
            clearFile()
            readFile(data)
            remove()
            writeFile()
            print("**new list**")
            showItems()
            Items.clear()
        case "l":
            data = getFile()
           
            readFile(data)
            print("**list**")
            showItems()

            Items.clear()
            #list()
        case _:
            print("try c, r or l")

main()
