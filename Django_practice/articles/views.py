from os import name
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    context = {
        'name' : 'alex',
        'foods' : ['chicken','shrimp','fried'],
        'six_foods' : [food for food in foods if len(food) > 6]
    }

    return render(request, 'greeting.html', context)

def index2(request):
    return render(request, 'index2.html')

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # print(request)
    # print(type(request))
    #print(request.GET)
    department = request.GET.get('department')
    name = request.GET.get('name')

    if department == '대전 2반' or department == '대전2반':
        message = "교육생이시군요"
    else:
        message = "다른 반이시군요"

    context = {
        'message' : message,
    }

    return render(request, 'catch.html', context)

def show(request, name):
    context = {
        'name' : name
    }

    return render(request, 'show.html', context)