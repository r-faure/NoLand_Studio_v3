from django.shortcuts import render
from Home.models import Homelink, categorieslink


def home(request):
    """ Afficher tous les liens vers les apps """
    homelinks = Homelink.objects.all() # selection de tous les articles
    categories = categorieslink.objects.all()
    return render(request, 'Home/home.html', {'homelinks': homelinks, 'categories': categories})