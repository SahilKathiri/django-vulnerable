from django.conf.urls import include, url

from . import views


app_name = 'countries'
urlpatterns = [
    # Non-auth views
    url(r'^$', views.index, name='index'),

]