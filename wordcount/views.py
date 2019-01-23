from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    #return 'Helo' #WILL NOT WORK
    #return HttpResponse('Hello')
    #return render(request, 'home.html', {'hithere':'This is me'})
    return render(request, 'home.html')

#def eggs(request):
    #return HttpResponse('Eggs are great!')
#    return HttpResponse('<h1>EGGS</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulletxt)
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    # return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':worddictionary })
    # return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':worddictionary.items() })
    return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords })

def about(request):
    return render(request, 'about.html')
