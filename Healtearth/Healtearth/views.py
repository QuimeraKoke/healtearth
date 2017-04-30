from django.shortcuts import render

def index(request):
	return 

def form(request):
	if request.method == 'POST':
		print request
	return render(request, 'form.html')