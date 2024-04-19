# ==================================================> Imports <==================================================
# ----> genrel <----
from django.urls import path
from django.contrib.auth import views
from .views import *
# ----> external <----
from .views import *

app_name = 'account'
urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    #  ),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]

urlpatterns += [
    # path("update_user/",, name ="update_user"),
    path("register_user/",CreateUserView.as_view(), name ="register_user"),
    path("update_user/<int:pk>",UpdateUserView.as_view(), name ="update_user"),
    path("list_user/",ViewUserView.as_view(), name ="list_user"),

]
