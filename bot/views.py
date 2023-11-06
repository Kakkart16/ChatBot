from django.shortcuts import render
from django.http import JsonResponse
import openai


api_key = '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'
openai.api_key = api_key

def GPT(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.7,
    )
    
    answer = response.choice[0].text.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = GPT(message)
        return JsonResponse({'message':message, 'response':response})
    return render(request, 'chatbot.html')