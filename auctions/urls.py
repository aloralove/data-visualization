from django import forms
from django.urls import path
from django.urls import reverse

from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

from . import views, forms

from .views.index_views import IndexView
from .views.dashboard_views import DashboardView, UserProfileView, UserProfileUpdateView
from .views.comment_views import CommentCreateView

from django.contrib.auth import views as auth_views

from .views.dashboard_views import user_profile_view, edit_user_profile, upload_profile_picture

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('comment/', CommentCreateView.as_view(), name='add_comment'),
    path('register/', views.register, name="register"),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    
    path('profile/', user_profile_view, name='profile'),
    path('profile/edit/', edit_user_profile, name='edit_profile'),
    path('upload_picture/', upload_profile_picture, name='upload_profile_picture'),

    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=forms.MyPasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
