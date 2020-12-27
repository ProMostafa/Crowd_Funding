from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='account/change_password.html'),
         name='password_change'),
    path('change_password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='account/change_password_done.html'),
         name='password_change_done'),

    path('reset_password/', PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_done/', PasswordChangeDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('active/<uidb64>/<token>', views.ActiveAccountView.as_view(), name='active'),
    # profile
    path('profile', views.profile, name='profile_page'),
    path('update_user_information/', views.update_user_information, name='update_user_information'),
    path('update_project/<int:project_id>/', views.update_project, name='update_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('update_donation/<int:donation_id>/', views.update_donation, name='update_donation'),
    path('delete_donation/<int:donation_id>/', views.delete_donation, name='delete_donation'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('update_user_avatar/<int:user_id>/', views.update_user_avatar, name='update_user_avatar')
]
