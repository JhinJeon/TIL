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
    return render(request, 'catch.html')