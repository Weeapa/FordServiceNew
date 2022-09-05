from django.shortcuts import render
from django.http import HttpResponse

from team.models import Workers


def team(request):
    workers = Workers.objects.all()
    return render(request, 'team/index.html', {'workers': workers} )



# Create your views here.
