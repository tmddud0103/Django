from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    numbers = range(1, 46) 
    this_week = [1, 2, 3, 4, 5, 6]
    result = {
        0 : 0,
        1 : 0, 
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
    }

    for _ in range(1000):
        pick = random.sample(numbers, 6)
        match_count = len(set(pick) & set(this_week))
        result[match_count] += 1
    
    context = {
        'pick' : pick,
        'result' : result,
        
    }

    return render(request, 'lotto.html', context)