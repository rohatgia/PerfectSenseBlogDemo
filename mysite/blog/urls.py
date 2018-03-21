from django.urls import path
import views

urlpatterns = [
    path('^$', views.blog_posts, name='blog_posts'),
    path('^search', views.search, name='search'),
    path('^search/[?]q=$',views.blog_posts, name='blog_search'),
    path('^user/(?P<username>)', views.my_posts, name='my_posts'),
]