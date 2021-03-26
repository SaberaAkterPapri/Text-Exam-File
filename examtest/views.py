from django.shortcuts import render
from examtest.models import SearchEngine
from django.db.models import Count

# Create your views here.
def keyword_list(request):
    keywords = SearchEngine.objects.values('keyword').order_by('keyword').annotate(keyword_count=Count('keyword'))
    context = {
        'keywords' : keywords
    }   
    return render(request, 'search_list.html', context)


def search_list(request):
    keywords = SearchEngine.objects.all()
    context = {
        'keywords' : keywords
    }   
    return render(request, 'search_list.html', context)