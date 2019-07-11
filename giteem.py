#!/usr/bin/python3
# Author: Patrick Strube

# I saw a lot of other scripts that are far more flexible than this one, but I thought the world needed something a
# little more...focused?

# JSON pattern was initially generated with this lovely software: https://annihil.github.io/github-spray-generator/
# Pattern was then altered by me to look a bit easier to read while I'm developing

import json

GITHUB_BASE = "https://github.com"
JSON_FILE = "giteem-pattern.json"

ART = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 1, 1, 0, 0],
    [0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 1, 1, 0, 0],
    [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1, 1, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 2, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 1, 1, 0, 0]
]

def parseJsonPattern():
    # you better believe I'm not hand-coding that nested list
    with open(JSON_FILE, 'r') as jsonfile:
        data = json.load(jsonfile)
        row = 0
        for line in data:
            for char in line:
                ART[row].append(checkChar(char))
            print(ART[row])
            row += 1


def checkChar(ch):
    if ch == ' ':
        return 0
    elif ch == '#':
        return 4
    elif ch == '@':
        return 2
    elif ch == '|':
        return 1

parseJsonPattern()
