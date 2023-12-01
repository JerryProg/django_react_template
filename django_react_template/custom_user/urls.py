from django.urls import path
from custom_user.views import UsersList, CurrentUser

urlpatterns = [
    path('users_list/', UsersList.as_view(), name='users_list'),
    path('user/', CurrentUser.as_view(), name='user'),
]