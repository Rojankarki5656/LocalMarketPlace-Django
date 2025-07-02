from django.shortcuts import render

# Create your views here.
def user_messages(request):
	return render(request, 'usermessages/messages.html')