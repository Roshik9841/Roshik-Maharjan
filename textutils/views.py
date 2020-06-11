from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text','default')
    print(djtext)
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')

    if removepunc=="on":
        punctuations='''!()-{}';.'/[]?[.[;'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Removed punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover)=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char()
        params = {'purpose': 'remove newlines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (charcount) == "on":
        line = ""
        for char in text1:
            line = len(line)
    else:
        return HttpResponse("error")
