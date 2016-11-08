from bs4 import BeautifulSoup
import urllib2, os, re, codecs, time


# will save output to a file
def savefile(savethis):
        save = open('list.txt', 'a')
        for o in range(y):
            printit = ""
            for j in range(x):
                if x == 2:
                    printit =+ "  " + savethis[x][y] + "/n"
                else:
                    printit = savethis[x][y]
            save.write(printit)
        save.close()


# Checks findings against previous found records and removes them if they are the same
def checkfinds(findings):
    last = open('list.txt')
    for o in range(y):
        for j in range(x):
            checkit = findings[x][y]
            if checkit in last:
                del findings[x][y]
            print findings[x][y]
    savefile(findings)


# Sorts through html returns and removes undesired posts
def pickandchoose(choose):
    for a in choose:
        check = a.string
        if 'wanted' in check:
            a.append("Bad")  # del check['class']
        if '66' in check:
            craglist = check
            print craglist


def pull(link, relink, listof):
    b = 1
    content = urllib2.urlopen(link).read()
    soup = BeautifulSoup(content, "lxml")
    findthis = soup.find_all('a', 'hdrlnk', recursive=True)
    for a in findthis:
        listof[b][1] = a.string
        listof[b][2] = relink + a.get("href")
        print listof[b][1] + "  " + listof[b][2]
        b = + 1
    checkfinds(listof)


# def main():
    # this is where the main function will be, should be the "controller for the other functions"
    # craigslist search url
ctcraigslist = "http://hartford.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
nycraigslist = "http://newyork.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
    # pull link tag and add to end of craigslistrelink to create useable link
ctcraigslistrelink = "http://hartford.craigslist.org"
nycraigslistrelink = "http://newyork.craigslist.org"
listof = [[x for x in range(200)] for y in range(2)]
    # Changing links into array for easier automation, eventually it could/should be turned into a 2d array
links = ["http://hartford.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966", "http://newyork.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"]
relinks = ["http://hartford.craigslist.org", "http://newyork.craigslist.org"]

for i in range(len(links)):
    pull(links[i], relinks[i], listof)

    # content = urllib2.urlopen(ctcraigslist).read()
    # parsing data into soup variable
    # soup = BeautifulSoup(content, "lxml")

    # uncomment if you want to output the whole page
    # print soup.prettify()

    # compiles all of the post titles and links
    # findthis = soup.find_all('a', 'hdrlnk', recursive=True)
    # newposts = checkfinds(findthis, ctcraigslistrelink)
    # savefile(newposts, ctcraigslistrelink)
