from django.shortcuts import render
from django.views import generic
from .models import DeathNotice

class DeathNoticeList (generic.ListView):
    model = DeathNotice
    queryset = DeathNotice.objects.filter(status=1).order_by('-death_date')
    template_name = 'index.html'
    paginate_by = 6



