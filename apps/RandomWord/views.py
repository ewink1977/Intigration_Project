from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if request.method == 'GET':
        print('RANDOM GIBBERISH VIA GET REQUEST!')
        request.session['counter'] = 1
    if request.method == 'POST':
        print('RANDOM GIBBERISH VIA POST REQUEST')
        request.session['counter'] += 1
    random_gibberish = get_random_string(length=14)
    context = {
        'gibberish' : random_gibberish
    } 
    return render(request, 'random/index.html', context)

def reset(request):
    print('GIBBERISH COUNTER RESET')
    request.session.flush()
    return redirect('/')