from django.shortcuts import render

# Create your views here.
def dinner(request, menu, num):
    context = {
        'menu' : menu,
        'num' : num,
    }
    return render(request, 'pages/dinner.html', context)
    