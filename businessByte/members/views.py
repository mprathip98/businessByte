from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.utils.safestring import mark_safe

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('dashboard')

        else:
            messages.error(request, "Invalid Username or Password. Try Again.")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect('dashboard')

        else:
            for field, errors in form.errors.items():
                field1 = ""
                if field.isalnum() == True:
                    field1 = field[:-1]
                all_errors_list = []
                for error_text in errors:
                    all_errors_list.append(error_text)

                errors_html = f"<strong>{field1.capitalize()}:</strong><br><ul>"
                for item_text in all_errors_list:
                    errors_html += f"<li>{item_text}</li>"
                errors_html += "</ul>"

                print(errors_html)

                messages.error(request, mark_safe(errors_html))


            return redirect('register')

    else:
        form = UserRegisterForm()
        return render(request, "authenticate/register.html", {'form': form})
