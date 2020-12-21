from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        word = word.upper()
        print(word)
        if word in worddictionary:
            #Increment word count of word in worddictionary
            worddictionary[word] += 1
        else:
            #Add new word to dictionary
            worddictionary[word] = 1

    sortedcount = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(0))
    maxwords = len(sortedcount)
    sortedlist = []

    for order in range(maxwords):
        sortedlist.insert(order, sortedcount[order] + sortedwords[order])

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedlist': sortedlist})

def about(request):
    return render(request, 'about.html')
