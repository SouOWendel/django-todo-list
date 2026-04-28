from django.shortcuts import render, redirect

def register(request):
	pass

def sucesso(request):
	if request.user.is_authenticated:
		return redirect('index')
	return render(request, 'register/success.html')

def reset_pass(request):
	pass

def reset_success(request):
	if request.user.is_authenticated:
		return render(request, 'register/reset_success.html')
	return redirect('index')