from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from blogapp.models import BlogPost
def home_page(request):
	my_title = "Welcome to Try Django"
	qs = BlogPost.objects.all()[:5]
	context = {"title": my_title, "object_list": qs}
	return render(request, "home.html", context)

def about_page(request):
	my_title = "About Us..."
	return render(request, "about.html", {"title": my_title})

def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {"title": "Contact Us", "form": form}
	return render(request, "form.html", context)