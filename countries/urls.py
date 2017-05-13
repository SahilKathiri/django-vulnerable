from django.conf.urls import include, url

from . import views


app_name = 'countries'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.web_login, name='login'),
    url(r'^logout/$', views.web_logout, name='logout'),
	url(r'^auth/$', views.web_auth, name='login_auth'),

	url(r'^country/(?P<country>[a-zA-Z ]*)$', views.country_info, name='country_info'),
	

]