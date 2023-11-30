from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def userinput(request):
    return render(request, 'userinput.html')

def checkdata(request):
    email= request.GET['email']
    pas= request.GET['pas']
    data= {
        'email': email,
        'password': pas
    }

    return render(request, 'checkdata.html', data )