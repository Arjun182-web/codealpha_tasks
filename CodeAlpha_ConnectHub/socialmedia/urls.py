from django.urls import path
from . import views
from .views import edit_profile
from .views import create_post, feed

urlpatterns = [

    path('', views.home, name='home'),

    path(
    'profile/',
    views.profile_view,
    name='profile'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
    "edit-profile/",
    edit_profile,
    name="edit_profile"
    ),

    path(
    "feed/",
    feed,
    name="feed"
),

path(
    "create-post/",
    create_post,
    name="create_post"
),

path(
    "delete-post/<int:post_id>/",
    views.delete_post,
    name="delete_post"
),

path(
    "edit-post/<int:post_id>/",
    views.edit_post,
    name="edit_post"
),

path(
    'like/<int:post_id>/',
    views.like_post,
    name='like_post'
),

path(
    'comment/<int:post_id>/',
    views.add_comment,
    name='add_comment'
),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
]