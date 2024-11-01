from django.shortcuts import render
from visits.models import PageVisits

def home_page_view(request, *arg, **kwargs):
    querysets = PageVisits.objects.all()
    page_visits = PageVisits.objects.filter(path=request.path)
    PageVisits.objects.create(path=request.path)
    context_dict = {
        'my_title': 'my_page',
        'Total_vistis': querysets.count(),
        'page_visits': page_visits.count(),
        'page_visit_percenttange': (page_visits.count()*100)//querysets.count(),
        'querysets':querysets
    }
   
    return render(request, 'home.html', context_dict)