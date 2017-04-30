from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from models import Food
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
@require_http_methods(["POST"])
def search(request):
	text = request.POST[u'search_text']
	resp = Food.search(text)
	resp = [x.dict_rep() for x in resp]
	return JsonResponse({'results':resp}) 





