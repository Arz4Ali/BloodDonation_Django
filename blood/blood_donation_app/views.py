from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import ContactMessage, BloodRequest,BecomeDonor
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash,logout

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    success=False
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact_message.save()

        success=True
    return render(request, 'contact.html',{'success':success})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)

        login(request, user)
        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)

            if user:
                login(request, user)
                return redirect('profile')
            else:
                error = 'Invalid credentials'
        except User.DoesNotExist:
            error = 'User not found'
    else:
        error = None

    return render(request, 'login.html', {'error': error})



def profile(request):
    if request.user.is_authenticated:
        user = request.user

        if request.method == 'POST':
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')

            if not user.check_password(current_password):
                return render(request, 'profile.html', {
                    'user': user,
                    'error': 'Current password is incorrect.'
                })

            if new_password != confirm_new_password:
                return render(request, 'profile.html', {
                    'user': user,
                    'error': 'New passwords do not match!'
                })

            user.set_password(new_password)
            user.save()

            update_session_auth_hash(request, user)

            return render(request, 'profile.html', {
                'user': user,
                'success': 'Password changed successfully!'
            })

        return render(request, 'profile.html', {'user': user})

    else:
        return redirect('login')


def request_blood(request):
    success=False
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        blood_type = request.POST['blood_type']
        quantity = request.POST['quantity']
        reason = request.POST['reason']

        blood_request = BloodRequest(
            name=name,
            email=email,
            blood_type=blood_type,
            quantity=quantity,
            reason=reason
        )
        blood_request.save()

        success=True
    return render(request, 'blood_request_form.html',{'success':success})

def become_donor(request):
    success=False
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        blood_type = request.POST['blood_type']
        phone = request.POST['phone']
        address = request.POST['address']
        date_of_birth=request.POST['date_of_birth']
        preferred_donation_date=request.POST['preferred_donation_date']

        become_donor = BecomeDonor(
            name=name,
            email=email,
            blood_type=blood_type,
            phone=phone,
            address=address,
            date_of_birth=date_of_birth,
            preferred_donation_date=preferred_donation_date
        )
        become_donor.save()

        success=True
    return render(request,'become_donor_from.html',{'success':success})

def delete_account(request):
    if request.method == 'POST':
        confirm_email = request.POST.get('confirm_email')
        if confirm_email == request.user.email:
            user = request.user
            user.delete()
            logout(request)
            return redirect('login')
        else:
            return render(request, 'profile.html', {'error': 'Email confirmation failed.'})
    return redirect('profile')