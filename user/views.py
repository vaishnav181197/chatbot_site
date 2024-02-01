from django.shortcuts import render
from django.views.generic import TemplateView,View

# Create your views here.
class UserHomeView(TemplateView):
    template_name="userhome.html"

class ChatbotView(View):
    def get(self,request):
        return render(request,"chatbot.html")
