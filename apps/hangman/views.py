from django.shortcuts import render, redirect
from django.contrib import messages
import random

def index(request):
    if 'guesses' not in request.session:
        request.session['guesses'] = []
        request.session['attempts'] = 0
        request.session['random_word'] = []
        request.session['word'] = []
        request.session['status'] = False
    # selects random word
    word_list = ["monkey", "mouse", "bubble", "hawaii", "basketball", "chocolate", "starship", "platypus", "rainbows", "cheesecake", "banana", "copper", "chimpanzee", "bigfoot", "programmer"]
    number = random.randint(0,14)
    random_word = word_list[number]

    if not len(request.session['random_word']):
        for i in word_list[number]:
            request.session['random_word'].append(i)
            if i != " ":
                request.session['word'].append("_")
            else:
                request.session['word'].append(" ")
    return render(request, "hangman/index.html")

def guess_letter(request):
    qty_in_word = 0

    # checks for errors in guess
    if not request.POST['guess_letter'].isalpha():
        messages.warning(request, "Letters only")
    elif len(request.POST['guess_letter']) > 1:
        messages.warning(request, "You can only guess one letter")
    elif request.POST['guess_letter'] in request.session['guesses']:
        messages.warning(request, "You've already guessed this letter.")
    else: #If there are no errors, guess gets processed
        request.session['guesses'].append(request.POST['guess_letter'])
        request.session['attempts'] += 1

    # Checks if guess is in random_word and if so fills word with said letter in the appropriate spots
        if request.POST['guess_letter'] in request.session['random_word']:
            for i in range(len(request.session['random_word'])):
                if request.session['random_word'][i] == request.POST['guess_letter']:
                    request.session['word'][i] = request.session['random_word'][i]
                    qty_in_word+=1
                    if request.session['word'] == request.session['random_word']:
                            request.session['status'] = True

                        # messages.warning(request, "Hooray, you won!")
        else:
            messages.warning(request, "Try again")
    return redirect('hangman:index')

def reset(request):
    request.session.clear()
    return redirect('hangman:index')
