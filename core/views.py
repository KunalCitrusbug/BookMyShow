from django.shortcuts import render
from django.views.generic import View, DetailView
from core.models import Movie
from account.views import LoginRequired


# Create your views here.
class HomeView(View):
    template_name = "core/home2.html"
    model_class = Movie

    def get(self, *args, **kwargs):
        movie = self.model_class.objects.all()
        context = {"movie": movie}
        return render(self.request, self.template_name, context=context)


class MovieDetail(DetailView):
    model = Movie
    template_name = "core/movie_detail.html"

    def get(self, *args, **kwargs):
        movie = Movie.objects.get(pk=self.kwargs.get("pk"))
        return render(self.request, self.template_name, context={"movie": movie})
