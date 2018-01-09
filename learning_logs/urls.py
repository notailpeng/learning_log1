'''定義learning_logs的URL模式'''
from django.conf.urls import url
from . import views

app_name = 'learning_logs'
urlpatterns = [
	#主頁
	url(r'^$',views.index,name='index'),
	url(r'^topics/$',views.topics,name='topics'),
	url(r'^topics/(?P<topic_id>\d+)$', views.topic,name='topic'),
	url(r'^new_topic/$',views.new_topic,name='new_topic'),
	#用於添加新的條目的頁面
	url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
	#用於編輯條目的頁面
	url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
	
]
