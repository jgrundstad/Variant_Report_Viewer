from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from viewer.models import Bnid

# Create your views here.
def index(request):
  context = {}
  return render(request, 'viewer/index.html', context)


def bionimbus_ids(request):
  Bnids = Bnid.objects.order_by('-bnid')
  context = {'list_of_ids': Bnids}
  return render(request, 'viewer/bionimbus_ids.html', context)
