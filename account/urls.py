from django.urls import path
from account.views import SignUpView, LoginView, LogoutView

app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
