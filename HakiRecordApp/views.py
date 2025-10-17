from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Statement
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def record_statement(request):
    if request.method == "POST":
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        ID_Number = request.POST['ID_Number']
        DOB = request.POST['DOB']
        Address = request.POST['Address']
        Phone_Number = request.POST['Phone_Number']
        incident_type = request.POST['incident_type']
        incident_location = request.POST['incident_location']
        incident_date = request.POST['incident_date']
        incident_time = request.POST['incident_time']
        suspect_description = request.POST['suspect_description']
        incident_description = request.POST['incident_description']
        incident_evidence=request.FILES['incident_evidence']

        statement = Statement(
            Service_No=request.user,
            First_Name = First_Name,
            Last_Name = Last_Name,
            ID_Number = ID_Number,
            DOB = DOB,
            Address = Address,
            Phone_Number = Phone_Number,
            incident_type=incident_type,
            incident_location=incident_location,
            incident_date=incident_date,
            incident_time=incident_time,
            suspect_description=suspect_description,
            incident_description=incident_description,
            incident_evidence=incident_evidence,
        )
        statement.save()
    return render(request, 'Statement.html')


def login_fn(request):
    if request.method == 'POST':
        Service_Number = request.POST['Service_Number']
        login_password = request.POST['login_password']
        user = authenticate(request, username=Service_Number, password=login_password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

    return render(request, 'login.html')

@login_required(login_url='login')
def view_cases(request):
    statements = Statement.objects.all()
    return render(request, "view_statement.html", {"statements":statements})

def recent_actions(request):
    # Fetch recent 20 admin actions
    actions = LogEntry.objects.select_related('content_type', 'user').order_by('-action_time')[:20]
    return render(request, 'recent_actions.html', {'actions':actions})

def logout_view(request):
    logout(request)
    return redirect('homepage')
def contact(request):
    return render(request, 'contact.html')

def evidence_vault(request):
    statements = Statement.objects.all().order_by('-id')
    return render(request, 'evidence.html',{"statements":statements})