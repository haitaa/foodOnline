from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserForm
from .models import User

# Create your views here.


def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # Create the user using create_user method
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                firstName=firstName, lastName=lastName, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            return redirect('registerUser')
        else:
            return redirect('registerUser')
    else:
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/registerUser.html', context)
