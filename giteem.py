#!/usr/bin/python3
# Author: Patrick Strube

# I saw a lot of other scripts that are far more flexible than this one, but I thought the world needed something a
# little more...focused?

# JSON pattern was initially generated with this lovely software: https://annihil.github.io/github-spray-generator/
# Pattern was then altered by me to look a bit easier to read while I'm developing

import json
from datetime import datetime, timedelta
import itertools

GITHUB_BASE = "https://github.com"
JSON_FILE = "giteem-pattern.json"

ART = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0, 0, 2, 2],
    [0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2],
    [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2, 0, 2, 0, 2],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2],
    [4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 2, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 0, 0, 2]
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

def parseYear():
    # todo: input validation
    print("Enter a year that's good for getting people")
    print("""
                        Note: this is a full-width calendar affair, so a year where you don't have a ton of commits 
                        (or any) would probably work best.
                    """)
    yearStr = input("->> ")

    int_year_valid = int(yearStr) > 0 and int(yearStr) <= datetime.now().year
    while not yearStr.isnumeric() and not int_year_valid:
        print("Nope that doesn't look like a valid year to me. Let's try that again.")
        print("Enter a year that's good for getting people")
        print("""
                    Note: this is a full-width calendar affair, so a year where you don't have a ton of commits 
                    (or any) would probably work best.
                """)
        yearStr = input("->> ")

    return int(yearStr)

def find_first_sunday(year):
    date = datetime(year, 1, 1, 9)
    weekday = datetime.weekday(date)

    while weekday < 6:
        date = date + timedelta(1)
        weekday = datetime.weekday(date)

    return date

def get_repo_name():
    # todo: input validation for invalid names
    return input("Enter the name for the dummy repo: ")

def get_github_name():
    # todo: input validation
    return input("Enter your github username: ")


if __name__ == '__main__':
    print("Lets GIT this bread")

    year = parseYear()
    start_date = find_first_sunday(year)
    repo_name = get_repo_name()
    username = get_github_name()

    script_content = build_script(start_date, repo_name, username)
    save(script_content, 'giteem.sh')

    print('giteem.sh saved')
    print('Create a new repo named {0} at github.com/ahrGNUts and run the script'.format(repo_name))

