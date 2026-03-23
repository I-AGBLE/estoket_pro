from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


# ------------------------------------------- Sign Up View For User Registration -------------------------------------------
def signup_view(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST, request.FILES)  # include request.FILES
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('home')
    else:
        signup_form = CustomUserCreationForm()
    return render(request, 'signup.html', {'signup_form': signup_form})




# ------------------------------------------- Sign In View For User Registration -------------------------------------------
def index(request):
    return render(request, 'index.html')
