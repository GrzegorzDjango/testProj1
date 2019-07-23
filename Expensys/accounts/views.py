from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        # login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('business_trip_home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return redirect('business_trip_home')


# po logout chcemy iść do strony głównej
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')


# # po logout chcemy iść do strony głównej
# def startExp(request):
#     user = request.user
#     if user.is_authenticated:
#         return redirect('business_trip_home')
#     else:
#         return redirect('login')