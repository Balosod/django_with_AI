from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import openai, os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.

api_key = os.getenv("OPENAI_KEY",None)

class ChatBot(View):
    template_name = "app/main.html"
    
    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        if api_key is not None:
            openai.api_key = api_key
            data  = request.POST.get('data')
            #prompt = f"translate this text to arabic: {data}"
            prompt = data
            response  = openai.Completion.create(
                engine = 'text-davinci-003',
                prompt = prompt,
                max_tokens = 256,
                # stop=".",
                temperature=0.5   
            )
            bot_response =  response["choices"][0]["text"]
        return render(request,self.template_name,{"response":bot_response})
