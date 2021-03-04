from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from .models import BlogPost

from .forms import (
    BlogPostForm,
    BlogPostModelForm,
)



def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.all().filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blogapp/list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)

@staff_member_required
def blog_post_create_view(request):
    template_name = 'form.html'
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostForm()
    context = {"form": form}
    return render(request, template_name, context)


def blog_post_detail_view(request, post_slug):
    print(timezone.now())
    print(timezone.localtime())
    
    template_name = 'blogapp/detail.html'
    obj = get_object_or_404(BlogPost, slug = post_slug)
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, post_slug):
    template_name = 'form.html'
    obj = get_object_or_404(BlogPost, slug = post_slug)
    form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if post_slug != obj.slug:
            return redirect("http://127.0.0.1:8000/blog/{}/edit/".format(obj.slug))
    context = {'form':form, "title": f"Update { obj.title }"}
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, post_slug):
    template_name = 'blogapp/delete.html'
    obj = get_object_or_404(BlogPost, slug = post_slug)
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_publish_view(request, post_slug):
    template_name = 'blogapp/publish.html'
    obj = get_object_or_404(BlogPost, slug = post_slug)
    if request.method == "POST":
        obj.publish_date = timezone.now()
        obj.save()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)