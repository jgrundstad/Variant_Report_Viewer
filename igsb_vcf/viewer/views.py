from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from forms import BnidForm, SampleForm, CallerForm, VcfForm, CaseForm, UserForm
from viewer.models import Bnid, Sample, Caller, Vcf, Case
from access_tests import in_proj_user_group


def index(request):
  return render(request, 'viewer/index.html',{})


def register(request):
  registered = False
  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    if user_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
      registered = True
    else:
      print user_form.errors
  else:
    user_form = UserForm()
  return render(request, 'viewer/register.html', {'user_form': user_form,
    'registered': registered})


def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect('/viewer/')
      else:
        # user is inactive
        return HttpResponse("Sorry, your account is disabled.")
    else:
      # Bad login details
      print "Invalid login details: {0}, {1}".format(username, password)
      return HttpResponse("Invalid login details provided.")
  else:
    context = {}
    context.update(csrf(request))
    return render(request, 'viewer/login.html', context)


def restricted(request):
  context = {}
  return render(request, '/viewer/index.html', context)


def permission(request):
  context = {}
  return render(request, '/viewer/permission.html', context)


@user_passes_test(in_proj_user_group)
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/viewer/')


@user_passes_test(in_proj_user_group)
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
    return render_to_response('viewer/new_case.html', context,
        context_instance=RequestContext(request))


@user_passes_test(in_proj_user_group)
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
    return render_to_response('viewer/new_bionimbus_id.html', context,
        context_instance=RequestContext(request))


@user_passes_test(in_proj_user_group)
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
    return render_to_response('viewer/new_sample.html', context,
        context_instance=RequestContext(request))


@user_passes_test(in_proj_user_group)
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
    return render_to_response('viewer/upload_vcf.html', context,
        context_instance=RequestContext(request))

