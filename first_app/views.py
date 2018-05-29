from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from . import forms
# Create your views here.

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {"access_records":webpages_list}
	return render(request,'first_app/index.html',date_dict)
	#return HttpResponse("Hello World!")
    #my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
    #return render(request,'index.html',context=my_dict)
    #return render(request,'first_app/index.html',context=my_dict)

def form_name_view(request):
    form = forms.NewUserForm()

    if request.method == 'POST':
    	form = forms.NewUserForm(request.POST)
    	if form.is_valid:
    		#print("EMAIL: "+form.cleaned_data['name'])
    		#print("TEXT: "+form.cleaned_data['url'])
    		form.save(commit=True)
    	else:
    		print("Error Occur")


    return render(request,'first_app/form_page.html',{'form':form})
        #form = forms.NewUserForm(request.POST)
        #if form.is_valid():
            # DO SOMETHING CODE
         #   print("VALIDATION SUCCESS!")
            #print("NAME: "+form.cleaned_data['topic'])
          #  print("EMAIL: "+form.cleaned_data['name'])
           # print("TEXT: "+form.cleaned_data['url'])
            #form.save(commit=True)
            #return index(request)
        #else:
		#	print("Error Occur")
	#return render(request,'first_app/form_page.html',{'form':form})	
	
def form_name_view2(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'first_app/form_page.html',{'form':form})

# Create your views here.
def index_new(request):
    return render(request,'first_app/index_new.html')

def other(request):
    return render(request,'first_app/other.html')

def relative(request):
    return render(request,'first_app/relative_url_templates.html')

