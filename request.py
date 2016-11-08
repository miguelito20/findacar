from bs4 import BeautifulSoup
import urllib2, os, re, codecs, time


# will save output to a file
def savefile(savethis, x, y):
        save = open('list.txt', 'a')
        for j in range(x):
            printit = ""
            for o in range(y):
                if x == 2:
                    printit = "  " + savethis[j, o] + "/n"
                else:
                    printit = savethis[j, o]
                save.write(printit)
        save.close()


# Checks findings against previous found records and removes them if they are the same
def checkfinds(findings, x, y):
    global b
    last = open('list.txt')
    for o in range(x):
        if o > b:
            savefile(findings, x, y)
        for j in range(y):
            if findings[o][j] in last:
                findings.pop([o][j])   # delete function causing an index error, possibly switch to using numpy
            print findings[o][j]



# Sorts through html returns and removes undesired posts
def pickandchoose(choose):
    for a in choose:
        check = a.string
        if 'wanted' in check:
            a.append("Bad")  # del check['class']
        if '66' in check:
            craglist = check
            print craglist


def pull(link, relink, listof, x, y):
    global b
    content = urllib2.urlopen(link).read()
    soup = BeautifulSoup(content, "lxml")
    # uncomment if you want to output the whole page
    # print soup.prettify()
    findthis = soup.find_all('a', 'hdrlnk', recursive=True)
    for a in findthis:
        listof[b][0] = a.string
        listof[b][1] = relink + str(a.get("href"))
        # uncomment if you want to check data integrity within pull function
        print listof[b][0] + "  " + listof[b][1]
        b = + 1
    checkfinds(listof, x, y)


# def craigslistsearch():
# this is where the main function will be, should be the "controller for the other functions"
# This is just for maintenance to know what links are in the arrays
ctcraigslist = "http://hartford.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
nycraigslist = "http://newyork.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
# pull link tag and add to end of craigslistrelink to create useable link
ctcraigslistrelink = "http://hartford.craigslist.org"
nycraigslistrelink = "http://newyork.craigslist.org"
listof = [[0 for x in range(200)] for y in range(2)]
# Changing links into array for easier management, eventually it could/should be turned into a 2d list
links = [ctcraigslist, nycraigslist]
relinks =[ctcraigslistrelink, nycraigslistrelink]
b=0
for i in range(len(links)):
    pull(links[i], relinks[i], listof, x, y)
