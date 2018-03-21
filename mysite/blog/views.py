from models import post, category, user
from django.contrib.auth.models import User
from django.http import HttpResponse 
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, render_to_response, get_object_or_404

def blog_posts(request):
    posts = post.objects.order_by('date')
    return render(request,'blog/blog_posts.html', {'posts': posts})

def search(request):
    categories = request.GET.get('categories')
    author = request.GET.get('username')
    words = request.GET.get('q')
    choice = request.GET.get('sorttype')

    categoryid = category.objects.filter(category=categories)
    userid = user.objects.filter(username=author)
    wordsegment = post.objects.filter(content__contains=words)
    blog = post.objects.order_by('date')
        
    if not words and not author and categories:
        blog = post.object.filter(category=categories)
        print("1")
    elif not words and author and not categories:
        blog = post.object.filter(user=author)
        print("2")
    elif not words and author and categories:
        blog = post.objects.filter(category=categories,user=author)
        print("3")
    elif words and not author and not categories:
        blog = wordsegment
        print("4")
    elif words and author and not catgeories:
        blog = post.objects.filter(user=author,content__contains=words)
        print("5")
    elif words and not author and categories:
        blog = post.object.filter(category=categories,content__contains=words)
        print("6")
    elif words and author and categories:
        blog = post.object.filter(category=categories,user=author,content__contains=words)
        print("7")
    else:
        blog = post.object.order_by('date')
        print("8")
        
    if choice == "dateA":
        blog = blog.order_by('date')
    elif choice == "dateD":
        blog = blog.order_by('-date')
    else:
        blog = blog

    return render(request, 'blog/blog_posts.html', {'posts' : blog})

@login_required
def my_posts(request, username):
    userloc = get_object_or_404(User, useraname=request.user.username)
    username = get_object_or_404(user, username=request.userloc)
    post_list = post.objects.filter(user=username).values_list('blog', flat=True)
    blog_group = []
    for blog in post_list:
        blog_group.append(blog-5)
    posts = post.objects.filter(user__in=blog_group)
    return render(request, 'blog/blog_list.html', {'posts': posts})