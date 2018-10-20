from django.shortcuts import render, redirect
import requests,json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

def landing(request):
    return render(request, 'server/landing.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = {'token': request.POST['token'], 'ttl': request.POST['ttl']}
        token_response = requests.post('http://localhost:8000/api/token/', data=data)
        check_user = requests.get('http://localhost:8000/api/borrower/')
        print (check_user)
        return HttpResponse('Succesfully added token.')
    else:
        return redirect(landing)

def logout(request):
    return redirect(landing)

def dashboard(request):
    return render(request, 'server/dashboard.html')

def facility(request):
    facilities = requests.get('http://localhost:8000/api/facility')
    print(facilities.json())
    return render(request, 'server/facility.html', {'facilities': facilities.json()})

def view_facility(request):
    return render(request, 'server/view_facility.html')

@csrf_exempt
def add_facility(request):
    # if request.method == 'POST':
        data = {'name': request.POST['name'], 'status': request.POST['status'], 'quantity': request.POST['quantity']}
        print (data)
        add_facility = requests.post('http://localhost:8000/api/facility/', data=data)
        print (add_facility)

        facilities = requests.get('http://localhost:8000/api/facility')
        print(facilities.json())
        return render(request, 'server/facility.html', {'facilities': facilities.json()})
    # elif request.method == 'GET':
    #     return render(request, 'server/add_facility.html')

@csrf_exempt
def del_facility(request, pk):
    url = requests.post('http://localhost:8000/api/status0/' + pk  )
    facilities = requests.get('http://localhost:8000/api/facility')
    print(facilities.json())
    return render(request, 'server/facility.html', {'facilities': facilities.json()})

@csrf_exempt
def act_facility(request, pk):
    url = requests.post('http://localhost:8000/api/status1/' + pk  )
    facilities = requests.get('http://localhost:8000/api/facility')
    print(facilities)
    return render(request, 'server/facility.html', {'facilities': facilities.json()})

@csrf_exempt
def edit_facility(request, pk):
    # if request.method == 'GET':
    #     url = 'http://localhost:8000/api/facilityss/' + pk 
    #     print (url)
    #     response = requests.get(url)
    #     print (response.json())
    #     return render(request,{'response': response.json()})
    # elif request.method == 'POST':
        url = 'http://localhost:8000/api/edit/' + pk 
        print (url)
        data = {'name': request.POST['name'], 'status': request.POST['status'], 'quantity': request.POST['quantity']}
        print (data)
        edited_facility = requests.post(url, data=data)
        facilities = requests.get('http://localhost:8000/api/facility')
        print(facilities.json())
        return render(request, 'server/facility.html', {'facilities': facilities.json()})

def equipment(request):
    equipments = requests.get('http://localhost:8000/api/equipment/')
    return render(request, 'server/equipment.html', {'equipments': equipments.json()})

@csrf_exempt
def add_equipment(request):
    if request.method == 'POST':
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        response = requests.post('http://localhost:8000/api/equipment/', data=data)
        print (response)
        return redirect(equipment)
    elif request.method == 'GET':
        return render(request, 'server/add_equipment.html')

@csrf_exempt
def edit_equipment(request, pk):
    if request.method == 'GET':
        url = 'http://localhost:8000/api/equipment/' + pk + '/'
        print (url)
        response = requests.get(url)
        print (response)
        return render(request, 'server/edit_equipment.html', {'equipment': response.json()})
    elif request.method == 'POST':
        url = 'http://localhost:8000/api/equipment/' + pk + '/'
        print (url)
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        edited_equipment = requests.put(url, data=data)
        return redirect(equipment)