from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from django.shortcuts import get_object_or_404


def homepage(request):

    # If user is already authenticated, no need to show login page again
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'homepage.html', {'records': records})

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Felicidades, haz ingresado")
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect. Please try again.")
            return redirect('home')

    return render(request, 'homepage.html')

def logout_user(request):
    logout(request)  # This logs the user out.
    return redirect('home')  # Redirects the user to the homepage after logout.

def customer_record(request, pk):
    if request.user.is_authenticated:
        # lookup records
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': record})
    else:
        messages.success(request, "Debes haber hecho log In para ver esa pagina")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, pk=pk)
        record.delete()
        messages.success(request, "Record deleted successfully.")
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to delete records.")
        return redirect('home')
    
def add_record(request):
    if request.method == 'POST':
        # Extract data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        ph_name = request.POST.get('ph_name')
        cellphone_number = request.POST.get('cellphone_number')
        email_address = request.POST.get('email_address')
        
        # Check if any field is empty
        if not (first_name and last_name and ph_name and cellphone_number and email_address):
            messages.error(request, "All fields are required.")
            return redirect('add_record')
        
        # Save to the database
        record = Record(
            first_name=first_name,
            last_name=last_name,
            ph_name=ph_name,
            cellphone_number=cellphone_number,
            email_address=email_address
        )
        record.save()

        # Redirect to homepage after saving
        return redirect('home')

    return render(request, 'add_record.html')

def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    
    if request.method == 'POST':
        # Extract data from POST request and update the record
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        ph_name = request.POST.get('ph_name')
        cellphone_number = request.POST.get('cellphone_number')
        email_address = request.POST.get('email_address')
        
        # Update the fields
        record.first_name = first_name
        record.last_name = last_name
        record.ph_name = ph_name
        record.cellphone_number = cellphone_number
        record.email_address = email_address
        record.save()

        messages.success(request, "Record updated successfully.")
        return redirect('record', pk=record.id)

    return render(request, 'edit_record.html', {'record': record})
