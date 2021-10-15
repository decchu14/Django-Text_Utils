# i have created this file - DashlineDsouza
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    params = {}
    purpose = ""

    if not(djtext):
        analysed = "Please enter the text in text area"
        params = {'purpose': 'Error', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)


    if removepunc == 'on':
        punctuations = '''!@#$%^&*()_-+=`~{}[]|\:;"'<>?/.,'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed+char
        purpose = purpose + ' Remove Punctuations'
        params = {'purpose' : purpose , 'analysed_text' : analysed}
        djtext = analysed

    if fullcaps == 'on':
        analysed = ""
        for char in djtext:
            analysed = analysed+char.upper()
        purpose = purpose + ' changed to upper case'
        params = {'purpose': purpose, ' analysed_text': analysed}
        djtext = analysed

    if extraspaceremover == 'on':
        analysed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed = analysed+char

        purpose = purpose + ' removed extra spaces'
        params = {'purpose': purpose, 'analysed_text': analysed}
        djtext = analysed

    if charcount == 'on':
        count = 0
        for char in djtext:
            if char != " ":
                count += 1
        analysed = f'{djtext} : The number of characters in the text is {str(count)}'
        purpose = purpose + ' character counter'
        params = {'purpose': purpose , 'analysed_text': analysed}

    if removepunc == 'off' and fullcaps == 'off' and newlineremover == 'off' and extraspaceremover == 'off' and charcount == 'off':
        analysed = "Please check at least one operation"
        params = {'purpose': 'Error', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    return render(request, 'analyse.html', params)