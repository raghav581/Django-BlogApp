from django.shortcuts import render
from blogapp.models import BlogPost
from .models import SearchQuery
# Create your views here.
def search_view(request):
    query = request.GET.get("q", None)
    user = None
    context = {"query": query}
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        blog_list = BlogPost.objects.search(query)
        context["blog_list"] = blog_list
        SearchQuery.objects.create(user=user, query = query)
    template_name = 'searches/view.html'
    
    return render(request, template_name, context)