#!/usr/bin/env python3
import argparse
import sys
import os

Args = []
Items = ["jam", "paint"]

createVar = "c"
remVar = "r"
listVar = "l"

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
        showItems()

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
    print("**new List**")
    showItems()

def list():
    print("**List**")
    showItems()

def argsToItems():

    for arg in Args:
        Items.append(arg)

def main():
    parseArgs()
    match Args[0] :
        case "c":
            create()
        case "r":
            remove()
        case "l":
            list()
        case _:
            print("try c, r or l")

main()
