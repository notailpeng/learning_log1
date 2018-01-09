from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
	'''註銷用戶'''
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
	'''註冊新用戶'''
	if request.method != 'POST':
		#顯示空的註冊表單
		form = UserCreationForm()
	else:
		#處理填寫好的表單
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#讓用戶自動登錄，再重定向到主業
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form':form}
	return render(request, 'users/register.html', context)