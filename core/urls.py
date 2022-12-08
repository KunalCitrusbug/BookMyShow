from django.urls import path
from .views import HomeView,MovieDetail

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('movie/<int:pk>', MovieDetail.as_view(), name="movie_detail"),
]
