from bs4 import BeautifulSoup
from apiclient import discovery
import datetime
import cPickle as pickle
import urllib2, re, codecs, time, threading

#turns off program for a half an hour and checks if its tomorrow every half an hour - also set up with cron
def sleep():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    while datetime.date.today() < tomorrow:
        time.sleep(1800)
# will save output to a file
def savefile(savethis):
    pickle.dump(savethis, open('today.pickle','wb'))
    with open('today.txt', 'wb') as f:
        for (k, v) in savethis.items():
            line = '{}, {}'.format(k, v) 
            f.write(line + "\n")
# Checks findings against previous found records and removes them if they are the same

def listsave(listit):
     with open('list.txt', 'wb') as f:
        for (k, v) in listit.items():
            line = '{}, {}'.format(k, v) 
            f.write(line + "\n")

def checkfinds():
    checkit={}  
    ps = {}
    ts = {}
    #load list through pickle as its faster
    ps = pickle.load( open( "list.pickle", "rb" ))
    listsave(ps)
    # print ps.values() # break point to check the proper loading of data into the dictionary
    for k in carDict.keys(): #checking to see if the keys from past search exist in the new search results
        if ps.has_key(k) != True:
            checkit[k] = carDict.get(k, "error") # pushing anything not found into secondary dictionary for crosschecking
    carDict.clear() #emptying array for later use as all data stored should have been split to old results or check against yesterdays results
    ts = pickle.load(open('today.pickle', 'rb'))
    for k in checkit.keys():
        if ts.has_key(k) != True:
            carDict[k] = checkit.get(k, "error")
    pickle.dump(ts, open('list.pickle', 'a+b'))
    return savefile(carDict)


# Sorts through html returns and removes undesired posts
def pickandchoose(choose):
    for (k,v) in choose.items():
        if 'wanted' or "parts" in v: #add any text screening
            del choose [k]
    return checkfinds()

def pull(link, relink):
    content = urllib2.urlopen(link).read()
    soup = BeautifulSoup(content, "html5lib")
    # uncomment if you want to output the whole page
    # print soup.prettify()
    findthis = soup.find_all('a', 'hdrlnk', recursive=True)
    for a in findthis:
        carDict[str(relink + a.get("href"))] = a.string
        # print carDict.items() # break point to check if data is parsing through properly
    return pickandchoose(carDict)


# this is where the main function will be, should be the "controller for the other functions"
# This is just for maintenance to know what links are in the arrays
ctcraigslist = "http://hartford.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
nycraigslist = "http://newyork.craigslist.org/search/cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
craigslistparams = "cta?auto_make_model=ford%20mustang&hints=makemodel&min_auto_year=1966"
carDict = {}
# pull link tag and add to end of craigslistrelink to create useable link
ctcraigslistrelink = "http://hartford.craigslist.org"
nycraigslistrelink = "http://newyork.craigslist.org"

#setting threading objects
ctcraigObj = threading.Thread(target=pull(ctcraigslist, ctcraigslistrelink))
nycraigObj = threading.Thread(target=pull(nycraigslist, nycraigslistrelink))
sleepObj = threading.Thread(target=sleep())

#Activating threading objects
ctcraigObj.start
nycraigObj.start
sleepObj.start

# Changing links into array for easier management, eventually it could/should be turned into a 2d list
#links = [ctcraigslist, nycraigslist]
#relinks =[ctcraigslistrelink, nycraigslistrelink]
#for i in range(len(links)):
#    pull(links[i], relinks[i])
