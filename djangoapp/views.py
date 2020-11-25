from django.shortcuts import render

def formpage(request):
    return render(request,"djangoapp/form.html")

def result(request):
    if request.POST.get('name'):
        name_from_form = request.POST['name']
    else:
        name_from_form = ""
    if request.POST.get('email'):
        email_from_form = request.POST['email']
    else:
        email_from_form = ""
    if request.POST.get('language'):
        language_from_form = request.POST['language']
    else:
        language_from_form = ""
    if request.POST.get('country'):
        country_from_form = request.POST['country']
    else:
        country_from_form = ""
    if request.POST.get('optradio'):
        optradio_from_form = request.POST['optradio']
    else:
        optradio_from_form = ""
    if request.POST.get('two'):
        two_from_form = request.POST['two']
    else:
        two_from_form = ""
    if request.POST.get('three'):
        three_from_form = request.POST['three']
    else:
        three_from_form = ""
    if request.POST.get('one'):
        one_from_form = request.POST['one']
    else:
        one_from_form = ""     
    if request.POST.get('Optional'):
        Optional_from_form = request.POST['Optional']
    else:
        Optional_from_form = ""

    context = {
    "name_on_template" : name_from_form,
    "email_on_template" : email_from_form,
    "language_from_form" :language_from_form,
    "country_from_form" : country_from_form,
    "optradio_from_form" :optradio_from_form,
    "one_from_form" : one_from_form,
    "two_from_form":two_from_form,
    "three_from_form" : three_from_form,
    "Optional_from_form" : Optional_from_form

    }
    return render(request,"djangoapp/show.html",context )