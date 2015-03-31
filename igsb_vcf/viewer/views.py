from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from forms import BnidForm, SampleForm, CallerForm, VcfForm, CaseForm
from viewer.models import Bnid, Sample, Caller, Vcf, Case

# Create your views here.
def index(request):
  context = {}
  return render(request, 'viewer/index.html', context)

def new_case(request):
  if request.method == 'POST':
    cform = CaseForm(request.POST, instance=Case())
    if cform.is_valid():
      cform.save()
    return HttpResponseRedirect('/viewer/new_case/')
  else:
    cform = CaseForm(instance=Case())
    context = {'case_form': cform}
    cases = Case.objects.all()
    context['cases'] = cases
    context.update(csrf(request))
    return render_to_response('viewer/new_case.html', context)


def bionimbus_ids(request):
  Bnids = Bnid.objects.order_by('-bnid')
  context = {'list_of_ids': Bnids}
  return render(request, 'viewer/bionimbus_ids.html', context)

def upload_vcf(request):
  if request.method == 'POST':

    form = VcfForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      
      return HttpResponseRedirect('viewer/index.html')
  
  else:
    form = VcfForm()

  return render_to_response('viewer/upload_vcf.html', locals())

