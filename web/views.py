from django.shortcuts import render
from .models import Anounce
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def index(request):
	return render(request, 'index.html', {})

def contact(request):
	return render(request, 'contact/contact.html', {})

def anounce(request):
	return render(request, 'anounce/anounce.html', {})

def anounce_view(request):
	return render(request, 'anounce/anounce_view.html', {})

@csrf_exempt
def get_list(request):
	anounce_list = Anounce.objects.order_by('-created').values()
	return JsonResponse({"result":list(anounce_list)})


@csrf_exempt
def detail_list(request, num):
	detail_list = Anounce.objects.filter(id=num).values()
	return JsonResponse({"result":list(detail_list)})

