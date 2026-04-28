from django.shortcuts import render, redirect
from .forms import MyPasswordChangeForm, MyUserCreationForm
from django.contrib.auth import update_session_auth_hash

def register(request):
	if request.user.is_authenticated:
		return redirect('index')
	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = MyUserCreationForm()
	return render(request, 'register/register.html', {'form': form})

def success(request):
	if request.user.is_authenticated:
		return redirect('index')
	return render(request, 'register/success.html')

def reset_pass(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = MyPasswordChangeForm(user=request.user, data=request.POST)
			if form.is_valid():
				user = form.save()
				update_session_auth_hash(request, user)
				return redirect('reset_success')
		else:
			form = MyPasswordChangeForm(request.user)
			return render(request, 'register/reset_pass.html', {'form': form})
	
	return redirect('index')

def reset_success(request):
	if request.user.is_authenticated:
		return render(request, 'register/reset_success.html')
	return redirect('index')