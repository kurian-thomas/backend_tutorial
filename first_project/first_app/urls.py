from django.conf.urls import url
from django.contrib import admin
from first_app import views
from django.conf.urls import include

urlpatterns = [
	url(r'^index/',views.index,name='index'),
	url(r'^form_page/',views.entry,name='form'),
	url(r'^user_signup/',views.signup,name='form'),
	]