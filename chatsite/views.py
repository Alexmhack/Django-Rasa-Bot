from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .bot import agent

def home_view(request):
	return render(request, 'home_view.html')


@csrf_exempt
def handle_response(request, *args, **kwargs):
	if request.method == "POST":
		print(request)
		print(kwargs)
		responses = agent.handle_message(message)
		print(responses)
		return JsonResponse(responses)
