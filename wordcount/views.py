from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html",{'hithere':'SEE YOU!'})
def about(request):
    return render(request, "about.html")

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddictionary= {}
    for i in wordlist:
        if i in worddictionary:
            worddictionary[i] +=1
        else:
            worddictionary[i] = 1

    sortedwords = sorted(worddictionary.items(),key = operator.itemgetter(1), reverse = True)
    return render(request, "count.html", {'fulltext':fulltext, 'count':len(wordlist),  'worddictionary': worddictionary,'sortedwords':sortedwords})
