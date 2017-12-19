from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='home'),
	url(r'^forum', views.forum, name='forum'),
	url(r'^about', views.about, name='about'),
]
