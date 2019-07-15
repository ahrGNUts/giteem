#!/usr/bin/python3
# Author: Patrick Strube

# I saw a lot of other scripts that are far more flexible than this one, but I thought the world needed something a
# little more...focused?

# JSON pattern was initially generated with this lovely software: https://annihil.github.io/github-spray-generator/
# Pattern was then altered by me to look a bit easier to read while I'm developing

import json
from datetime import datetime, timedelta
import itertools
import os

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

def generate_next_dates(start_date):
    """generator that returns the next date, requires a datetime object as
    input. The offset is in weeks"""
    start = 7
    for i in itertools.count(start):
        yield start_date + timedelta(i)

def generate_values_in_date_order():
        height = 7
        width = len(ART[0])

        for w in range(width):
            for h in range(height):
                yield ART[h][w]

def commit(commitdate):
    template = (
        '''GIT_AUTHOR_DATE={0} GIT_COMMITTER_DATE={1} '''
        '''git commit --allow-empty -m "giteem" > /dev/null\n'''
    )
    return template.format(commitdate.isoformat(), commitdate.isoformat())

def build_script(start_date, repo_name, username):
    template = (
        '#!/usr/bin/env bash\n'
        'REPO={0}\n'
        'git init $REPO\n'
        'cd $REPO\n'
        'touch README.md\n'
        'git add README.md\n'
        'touch giteem\n'
        'git add giteem\n'
        '{1}\n'
        'git remote add origin {2}:{3}/$REPO.git\n'
        'git pull origin master\n'
        'git push -u origin master\n'
    )

    strings = []
    for value, date in zip(generate_values_in_date_order(),
                           generate_next_dates(start_date)):
        for _ in range(value):
            strings.append(commit(date))

    return template.format(repo_name, ''.join(strings), "git@github.com", username)

def save_commit_script(output, filename):
    # save shell script that will create the commits for the art
    with open(filename, 'w') as f:
        f.write(output)
    os.chmod(filename, 0o755)  # add execute permissions

if __name__ == '__main__':
    print("Lets GIT this bread")

    year = parseYear()
    start_date = find_first_sunday(year)
    repo_name = get_repo_name()
    username = get_github_name()

    script_content = build_script(start_date, repo_name, username)
    save_commit_script(script_content, 'giteem.sh')

    print('giteem.sh saved')
    print('Create a new repo named {0} at github.com/ahrGNUts and run the script'.format(repo_name))

