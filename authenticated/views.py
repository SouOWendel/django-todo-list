from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
	if request.user.is_authenticated:
		return redirect('index')
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				form.add_error('username', 'Credenciais inválidas.')
				return render(request, 'authenticated/login.html', {'form': form})
		else:
			return render(request, 'authenticated/login.html', {'form': form})
	form = LoginForm()
	return render(request, 'authenticated/login.html', {'form': form})

@login_required(login_url='login_page')
def logout_page(request):
	logout(request)
	return redirect('index')