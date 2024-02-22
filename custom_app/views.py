from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required


 
# Views
@login_required
def home(request):
    # username = request.session['username']
    return render(request, "registration/success.html")
 
def register(request):
    if request.method == 'POST':    
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username = username, password = password)
        login(request, user)
        # request.session['username'] = username
        # request.session['password'] = password
        return redirect('home')
    
    return render(request, 'registration/register.html')

