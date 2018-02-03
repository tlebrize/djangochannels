from django.shortcuts import render

def main(request):
	return render(request, 'chat/main.html', {})

def profile(request):
	if request.user.is_authenticated:
		username = request.user.username
	else:
		username = 'Anonymous'
	return render(request, 'chat/profile.html', {'username': username})
