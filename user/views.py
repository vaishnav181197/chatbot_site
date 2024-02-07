from django.shortcuts import render
from django.views.generic import TemplateView,View
from .pro import chatbotfun

# Create your views here.
class UserHomeView(TemplateView):
    template_name="userhome.html"

class ChatbotView(View):
    def get(self,request):
        return render(request,"chatbot.html")
    def post(self,request):
        question=request.POST.get('qstn')
        res=chatbotfun(question)
        print(res)
        return render(request,"chatbot.html",{"result":res,"question":question})



