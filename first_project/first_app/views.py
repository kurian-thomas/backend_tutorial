from django.shortcuts import render
from django.http import HttpResponse 
from first_app.models import Topic,Webpage,AccessRecord 
from first_app import froms
# Create your views here.

def index(request):
	#return HttpResponse("hello world!")
	webpg_list=AccessRecord.objects.order_by('date')
	date_dic={'access_records':webpg_list,'insert_me':'from views'}
	#my_dic={'insert_me':"this from views"}
	return render(request,'first_app/index.html',context=date_dic)


def entry(request):
	form=froms.Formname()

	if request.method=='POST' :
		form=froms.Formname(request.POST)
		if form.is_valid():
			print("VALIDATION SUCCESS")
			print("name: "+form.cleaned_data['name'])
			print("email: "+form.cleaned_data['email'])
			print("text: "+form.cleaned_data['text'])
	else:
		print("not valid")	

	return render(request,'first_app/form_page.html',{'form':form})
	# return render(request,'first_app/form_page.html')

def signup(request):
	form=froms.NewUserForm()

	if request.method=='POST' :
		form=froms.NewUserForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
	else:
		print("not valid")	

	return render(request,'first_app/form_page.html',{'form':form})
	# return render(request,'first_app/form_page.html')