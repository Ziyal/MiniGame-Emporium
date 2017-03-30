from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'madlibs/index.html')

def process(request):
    if request.method == "POST":

        request.session['data'] = {
        "value1": request.POST['value1'],
        "value2": request.POST['value2'],
        "value3": request.POST['value3'],
        "value4": request.POST['value4'],
        "value5": request.POST['value5'],
        "value6": request.POST['value6'],
        "value7": request.POST['value7'],
        "value8": request.POST['value8'],
        "value9": request.POST['value9'],
        "value10": request.POST['value10'],
        "value11": request.POST['value11'],
        "value12": request.POST['value12'],
        "value13": request.POST['value13'],
        "value14": request.POST['value14'],
        "value15": request.POST['value15'],
        "value16": request.POST['value16'],
        "value17": request.POST['value17'],
        "value18": request.POST['value18'],
        "value19": request.POST['value19']
        }
        for i in range(1,19):
            if not len(request.POST['value'+str(i)]):
                messages.warning(request, "All fields are required!")
                return redirect('madlibs:index')

        return render(request, 'madlibs/completed.html')

def clear_session(request):
    request.session.clear()
    return redirect('madlibs:index')

# def completed(request):
#     print request.session['data']
#     return render(request, 'madlibs/completed.html')
