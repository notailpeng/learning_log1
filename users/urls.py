'''定義users的URL模式'''
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

app_name = 'users'
urlpatterns=[
	#登錄頁面
	url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
	#註銷
	url(r'^logout/$' ,views.logout_view, name='logout'),
	#註冊頁面
	url(r'^register/$',views.register, name='register'),

	]