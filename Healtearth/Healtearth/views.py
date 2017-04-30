from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from API.models import Food

@require_http_methods(["GET"])
def index(request):
	return 

@require_http_methods(["GET", "POST"])
def form(request):
	if request.method == 'POST':
		print request.POST
		new_food = Food()
		new_food.name = request.POST[u'name']
		new_food.amount = int(request.POST[u'amount'])
		new_food.unit = request.POST[u'unit']
		new_food.air_pollution = int(request.POST[u'air'])
		new_food.water_pollution = int(request.POST[u'water'])
		new_food.garbage = int(request.POST[u'garbage'])
		new_food.grade = int(request.POST[u'grade'])
		new_food.save()
	return render(request, 'form.html')
