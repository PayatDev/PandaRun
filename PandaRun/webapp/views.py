from django.shortcuts import render
from webapp.forms import full_runner_form
from webapp.forms import half_runner_form
from webapp.forms import contact_form

from webapp.models import full_runner
from webapp.models import half_runner
from webapp.models import contact


# Create your views here.
def home(request):
    return render(request, 'webapp/home.html')

def result(request):
    return render(request, 'webapp/page_not_ready.html')

def gallery(request):
    return render(request, 'webapp/page_not_ready_two.html')

def FQA(request):
    return render(request, 'webapp/FQA.html')

def reward(request):
    return render(request, 'webapp/reward.html')

def schedule(request):
    return render(request, 'webapp/schedule.html')

def course(request):
    return render(request, 'webapp/course.html')

def regis_info(request):
    return render(request, 'webapp/regis_info.html')

def register(request):
    return render(request, 'webapp/register.html')

def full_regis(request):
    form = full_runner_form()
    if request.method == "POST":
        form = full_runner_form(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return thank(request)
        else:
            return error(request)
    return render(request, "webapp/full_regis.html", {'form':form})

def half_regis(request):
    form = half_runner_form()
    if request.method == "POST":
        form = half_runner_form(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return thank(request)
        else:
            return error(request)
    return render(request, "webapp/half_regis.html", {'form':form})

def thank(request):
    return render(request, 'webapp/thank.html')

def error(request):
    return render(request, 'webapp/error.html')

def check(request):
    if request.method == "POST":
        number = request.POST['your_number']
        checking_runner21 = full_runner.objects.filter(mobile = number)
        checking_runner10 = half_runner.objects.filter(mobile = number)
        runner_dict = {'checking21':checking_runner21, 'checking10':checking_runner10,}

        return render(request,'webapp/check.html', context = runner_dict)

    else:
        print("ERROR FORM INVALID")

    return render(request, 'webapp/check.html')

def contact(request):
    form = contact_form()
    if request.method == "POST":
        form = contact_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return sent(request)
        else:
            return error(request)
    return render(request, "webapp/contact.html", {'form':form})

def sent(request):
    return render(request, 'webapp/sent.html')
