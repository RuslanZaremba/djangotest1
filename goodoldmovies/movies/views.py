from django.shortcuts import render
from django.conf import settings
from django.views import View

movies = [
    {'title': 'Catchfire', 'year': 1990, },
    {'title': 'Mighty Ducks the Movie: The First Face-Off', 'year': 1997, },
    {'title': 'Le Zombi de Cap-Rouge', 'year': 1997, },
]

movies_data = {1: 'The Dark Knight', 2: '12 Angry Men', 3: 'Il buono, il brutto, il cattivo'}


def movie_view(request):
    context = {'movies': movies}
    return render(request, 'movies/index.html',
                  context=context)


def ex_view(request, text):
    context = {'data': text}
    return render(request, 'movies/example.html', context=context)


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html', {'name': 'Alex', 'place': 'Lab'})


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html', {})
