#!/usr/bin/env python3
import argparse
import sys
import os


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to data.txt
data_file_path = os.path.join(script_dir, 'data.txt')


List = []
def getData():
    with open(data_file_path ) as file:
        data = file.readline().strip()
    return data

def parseData(data):
    item = ""
    for i in range(len(data)):
        if data[i] != '|':
            item = item + data[i]
        #    print(item)
        else:
            List.append(item)
            item = ""

def showList():
    index = 0
    for x in List:
        print(str(index) , " " + x)
        index = index + 1

def emptyData():
    with open(data_file_path , 'w') as f:
        pass


def writeData():
    emptyData()
    with open(data_file_path , 'w') as f:
        for x in List:
            f.write(x+'|')

def createTask(strn):
    data = getData()
    parseData(data)
    List.append(strn)
    writeData()
    showList()

def remTask(num):
    data = getData()
    parseData(data)
    emptyData()
    index = 0
    for x in List:
        if x == num or str(index) == num:
            List.remove(x)
        index + 1
    writeData()
    showList()


def showData():
    with open(data_file_path , 'r') as f:
        
        for line in f:
            print(line)

def main():
    parser = argparse.ArgumentParser(description="A simple terminal tool.")
    parser.add_argument("action", help="The action to perform", choices=["c","l","r"])

    parser.add_argument("name", help="task name", nargs="?")

    args = parser.parse_args()


    if args.action == "c" and not args.name:
        parser.error("ERR")

    match args.action:
        case "c":
            createTask(args.name)
        case "l":
            #showData()
            data = getData()
            parseData(data)
            showList()


        case "r":

            remTask(args.name)
        case _:
            print("default case")
main()
