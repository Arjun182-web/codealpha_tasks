from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .forms import RegisterForm, ProfileUpdateForm
from .forms import PostForm
from .models import Post
from .models import Like
from django.shortcuts import get_object_or_404
from .models import Comment
from .forms import CommentForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):

    posts = Post.objects.all().order_by('-created_at')

    return render(
        request,
        'feed.html',
        {
            'posts': posts
        }
    )


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":

        form = AuthenticationForm(
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'login.html',
        {'form': form}
    )

@login_required
def profile_view(request):

    profile = request.user.profile

    return render(
        request,
        'profile.html',
        {
            'profile': profile
        }
    )

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = ProfileUpdateForm(instance=profile)

    return render(
        request,
        "edit_profile.html",
        {"form": form}
    )

@login_required
def create_post(request):

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect("feed")

    else:

        form = PostForm()

    return render(
        request,
        "create_post.html",
        {
            "form": form
        }
    )


@login_required
def edit_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect("feed")

    else:

        form = PostForm(instance=post)

    return render(
        request,
        "edit_post.html",
        {
            "form": form,
            "post": post
        }
    )

    
@login_required
def feed(request):

    posts = Post.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "feed.html",
        {
            "posts": posts
        }
    )

@login_required
def like_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    like = Like.objects.filter(
        user=request.user,
        post=post
    )

    if like.exists():
        like.delete()
    else:
        Like.objects.create(
            user=request.user,
            post=post
        )

    return redirect("feed")


@login_required
def add_comment(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == "POST":

        text = request.POST.get("text")

        if text:

            Comment.objects.create(
                user=request.user,
                post=post,
                text=text
            )

    return redirect("feed")


@login_required
def delete_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    post.delete()

    return redirect("feed")

def logout_view(request):

    logout(request)

    return redirect('login')


