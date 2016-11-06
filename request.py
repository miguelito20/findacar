from bs4 import BeautifulSoup
import urllib2, os, re, codecs, time


# will save output to a file
def savefile(savethis, link):
        save = open('list.txt', 'a')
        for a in savethis:
            printit = a.string + "  " + link + a.get('href') + "\n"
            save.write(printit)
        save.close()


# Checks findings against previous found records and removes them if they are the same
def checkfinds(findings, link):
    last = open('list.txt')
    for a in findings:
        checkit = a.string + "   " + link + a.get('href')
        if checkit in last:
            del checkit
    last.close()
    savefile(findings, link)


# Sorts through html returns and removes undesired posts
def pickandchoose(choose):
    for a in choose:
        check = a.string
        if 'wanted' in check:
            a.append("Bad")  # del check['class']
        if '66' in check:
            craglist = check
            print craglist


def pull(link, relink):
    content = urllib2.urlopen(link).read()
    soup = BeautifulSoup(content, "lxml")
    findthis = soup.find_all('a', 'hdrlnk', recursive=True)

    checkfinds(findthis, relink)


# def main():
    # this is where the main function will be, should be the "controller for the other functions"
    # craigslist search url
ctcraigslist = "http://hartford.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
nycraigslist = "http://newyork.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
    # pull link tag and add to end of craigslistrelink to create useable link
ctcraigslistrelink = "http://hartford.craigslist.org"
nycraigslistrelink = "http://newyork.craigslist.org"

    # Changing links into array for easier automation, eventually it could/should be turned into a 2d array
links = ["http://hartford.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966", "http://newyork.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"]
relinks = ["http://hartford.craigslist.org", "http://newyork.craigslist.org"]

for i in links:
    pull(links[i], relinks[i])

    # content = urllib2.urlopen(ctcraigslist).read()
    # parsing data into soup variable
    # soup = BeautifulSoup(content, "lxml")

    # uncomment if you want to output the whole page
    # print soup.prettify()

    # compiles all of the post titles and links
    # findthis = soup.find_all('a', 'hdrlnk', recursive=True)
    # newposts = checkfinds(findthis, ctcraigslistrelink)
    # savefile(newposts, ctcraigslistrelink)
