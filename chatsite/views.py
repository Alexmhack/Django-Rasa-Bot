from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# from .bot import agent

def home_view(request):
	return render(request, 'index.html')


@csrf_exempt
def webhook(request):
	print(request.POST)
	return JsonResponse({"status": "OK"})


# # @csrf_exempt
# def handle_response(request, *args, **kwargs):
# 	if request.method == "POST":
# 		try:
# 			print(request)
# 			print(request.POST.get('user_input'))
# 			message = request.POST.get('user_input')
# 			responses = agent.handle_message(message)
# 			print(responses)
# 			bot_data = {
# 				'status': 'OK',
# 				'responses': responses[0]['text']
# 			}
# 			return JsonResponse(bot_data)
# 		except Exception as e:
# 			return JsonResponse({'status': 'FAILED'})
