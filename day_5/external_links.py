from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsobj,includeUrl):
    internalLinks = []
    for link in bsobj.findAll('a',href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['hren'] is not None:
            if link.attrs['href'] not in pages:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsobj, excludeUrl):
    externalLinks = []
    for link in bsobj.findAll('a',
                              href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace('http://','').split('/')
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsobj = BeautifulSoup(html,'lxml')
    externalLinks = getExternalLinks(bsobj,splitAddress(startingPage)[0])
    print(splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage,'')
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalLinks(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('The random external link is: '+externalLink)
    followExternalLinks(externalLink)

followExternalLinks('http://baike.baidu.com')