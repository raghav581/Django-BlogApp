from django.urls import path

from blogapp.views import (
    blog_post_list_view,
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_delete_view,
    blog_post_publish_view
)
urlpatterns = [
    path('', blog_post_list_view),
    path('<str:post_slug>/', blog_post_detail_view),
    path('<str:post_slug>/edit/', blog_post_update_view),
    path('<str:post_slug>/delete/', blog_post_delete_view),
    path('<str:post_slug>/publish/', blog_post_publish_view),
]