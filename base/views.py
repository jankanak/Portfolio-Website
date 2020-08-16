from django.shortcuts import render,redirect
from .models import Post,Tag
from .forms import PostForm
from .filters import PostFilter
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def home(request):
    posts=Post.objects.all()[0:3]
    context={'posts':posts}
    return render(request,'base/index.html',context)

def posts(request):
    posts=Post.objects.all()
    myfilter=PostFilter(request.GET,queryset=posts)
    posts=myfilter.qs

    #pagination
    page=request.GET.get('page')
    paginator=Paginator(posts,3)
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    context={'posts':posts,'myfilter':myfilter}
    return render(request,'base/posts.html',context)

def post(request,slug):
    post=Post.objects.get(slug=slug)
    context={'post':post}
    return render(request,'base/post.html',context)

def profile(request):
    return render(request,'base/profile.html')

#CRUD VIEWS
@login_required(login_url="home")
def createPost(request):
    form=PostForm()
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context={'form':form}
    return render(request,'base/post_form.html',context)

@login_required(login_url="home")
def updatePost(request,slug):
    post=Post.objects.get(slug=slug)
    form=PostForm(instance=post)
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context={'form':form}
    return render(request,'base/post_form.html',context)


@login_required(login_url="home")
def deletePost(request,slug):
    post=Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    context={'item':post}
    return render(request,'base/delete.html',context)