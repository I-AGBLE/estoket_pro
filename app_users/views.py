from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required


User = get_user_model()







# ------------------------------------------- Sign Up View -------------------------------------------
def signup_view(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST, request.FILES)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)

            # 👇 Role-based redirect AFTER signup (to setup pages)
            if user.user_type == 'freelancer':
                return redirect('app_main:freelancer_index')
            elif user.user_type == 'company':
                return redirect('app_main:company_index')
            else:
                return redirect('app_users:index')

    else:
        signup_form = CustomUserCreationForm()

    return render(request, 'signup.html', {'signup_form': signup_form})






# ------------------------------------------- Login View -------------------------------------------
def login_view(request):
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)

                if user.check_password(password):
                    login(request, user)

                    # 👇 Role-based redirect AFTER login (to dashboards)
                    if user.user_type == 'freelancer':
                        return redirect('app_main:freelancer_dashboard')
                    elif user.user_type == 'company':
                        return redirect('app_main:company_dashboard')
                    else:
                        return redirect('app_users:index')

                else:
                    login_form.add_error(None, "Invalid password")

            except User.DoesNotExist:
                login_form.add_error(None, "User with this email does not exist")

    return render(request, 'index.html', {'login_form': login_form})







@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user

        # ------------------- Delete Company image -------------------
        if hasattr(user, 'companies'):
            for company in user.companies.all():
                if company.company_image:
                    company.company_image.delete(save=False)

        # ------------------- Delete User avatar -------------------
        if hasattr(user, 'avatar') and user.avatar:
            user.avatar.delete(save=False)

        # ------------------- Finally delete user -------------------
        user.delete()

        return redirect('app_users:index')

    return redirect('app_main:freelancer_dashboard')