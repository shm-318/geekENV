from django.shortcuts import render

# Create your views here.
def BotView(request):
    return render(request,'bot/chatroom.html')