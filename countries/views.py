from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

from .forms import LoginForm, CommentForm
from .models import WebUser, Country, Comment

@login_required()
def index(request):
	context_dict = {}
	user = request.user
	web_user = WebUser.objects.get(user=user)
	context_dict['user'] = web_user

	if 'query' in request.GET:
		query = "SELECT * from countries_country WHERE countries_country.name "\
				"LIKE '{}'".format(request.GET.get('query'))
		country_list = Country.objects.raw(query)
	else:
		country_list = []

	# country_list = Country.objects.all().order_by('name')
	context_dict['country_list'] = country_list
	return render(request, 'countries/index.html', context_dict)

def web_login(request):
	form = LoginForm()
	context_dict = {'form': form}
	return render(request, 'countries/login.html', context_dict)

def web_logout(request):
	logout(request)
	return redirect('countries:logout')

def web_auth(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('countries:index')
			else:
				return HttpResponse('Your account is disabled')
		else:
			print("Invalid login details: {0}, {1}.".format(username, password))
			return HttpResponse("Invalid login details supplied")

	else:
		return render(request, 'countries/login.html', {})

@login_required()
def country_info(request, country):
	context_dict = {}
	user = request.user
	web_user = WebUser.objects.get(user=user)
	context_dict['user'] = web_user

	country = Country.objects.get(name=country)
	context_dict['country'] = country

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			body = form.cleaned_data['comment']
			Comment.objects.create(user=web_user, country=country, body=body)
			return redirect('countries:country_info', country=country.name)
	else:
		form = CommentForm()

	context_dict['form'] = form

	comments = Comment.objects.filter(country=country)
	context_dict['comments'] = comments

	return render(request, 'countries/country_info.html', context_dict)