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


def new_bionimbus_id(request):
  if request.method == 'POST':
    bform = BnidForm(request.POST, instance=Bnid())
    if bform.is_valid():
      bform.save()
    return HttpResponseRedirect('/viewer/new_bionimbus_id/')
  else:
    bform = BnidForm(instance=Bnid())
    context = {'bnid_form': bform}
    bnids = Bnid.objects.all().order_by('-bnid')
    context['bnids'] = bnids
    context.update(csrf(request))
    return render_to_response('viewer/new_bionimbus_id.html', context)


def new_sample(request):
  if request.method == 'POST':
    sform = SampleForm(request.POST, instance=Sample())
    if sform.is_valid():
      sform.save()
    return HttpResponseRedirect('/viewer/new_sample/')
  else:
    sform = SampleForm(instance=Sample())
    context = {'sample_form': sform}
    samples = Sample.objects.all()
    context['samples'] = samples
    context.update(csrf(request))
    return render_to_response('viewer/new_sample.html', context)



def upload_vcf(request):
  if request.method == 'POST':
    vform = VcfForm(request.POST, request.FILES)
    if vform.is_valid():
      vform.save()
      return HttpResponseRedirect('/viewer/upload_vcf/')
  else:
    vform = VcfForm(instance=Vcf())
    context = {'vcf_form': vform}
    vcfs = Vcf.objects.all()
    context['vcfs'] = vcfs
    context.update(csrf(request))
    return render_to_response('viewer/upload_vcf.html', context)

