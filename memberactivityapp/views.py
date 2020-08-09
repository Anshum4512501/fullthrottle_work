from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,UpdateView,DeleteView,DetailView,View
from memberactivityapp.forms import MemberCreateForm,ActivityCreateForm
from memberactivityapp.models import Members,Activity_Periods
from .mixins import SerializeMixin
from django.http import JsonResponse
# Create your views here.

class HomeView(TemplateView):
    template_name = 'memberactivityapp/home.html'
    
    def get_context_data(self,*args,**kwargs):
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context['members'] = Members.objects.all()
        return context
class MemberCreateView(CreateView):
    form_class = MemberCreateForm
    template_name = 'memberactivityapp/membercreate.html'
    success_url = '/'

class MemberUpdateView(UpdateView):
    model = Members
    form_class = MemberCreateForm
    pk_url_kwarg = 'pk'
    template_name = 'memberactivityapp/membercreate.html'
    success_url = '/'
class MemberDetailView(DetailView):
    model = Members
    pk_url_kwarg = 'pk'
    template_name = 'memberactivityapp/memberdetail.html'
    context_object_name = 'member'
    
class MemberDeleteView(DeleteView):
    model   = Members
    pk_url_kwarg = 'pk'
    template_name = 'memberactivityapp/confirmdelete.html'
    success_url = '/'

class ActivityCreateView(CreateView):
    form_class = ActivityCreateForm
    template_name = 'memberactivityapp/activity.html'
    success_url = '/'
    pk_url_kwarg = 'pk'
    def get_context_data(self,*args,**kwargs):
        context = super(ActivityCreateView,self).get_context_data(*args,**kwargs)
        context['member'] = Members.objects.get(id = self.kwargs.get('pk'))
        return context    
    def form_valid(self, form):
        print("Form instance",self.request.POST['members_id'])
        member = Members.objects.get(id=self.request.POST['members_id'])
        form.instance.members = member
        return super(ActivityCreateView, self).form_valid(form)    

class ActivityUpdateView(UpdateView):
    form_class = ActivityCreateForm
    model = Activity_Periods
    template_name = 'memberactivityapp/activity.html'
    success_url = '/'
    pk_url_kwarg = 'pk'
       
     

class ActivityDeleteView(DeleteView):
    model = Activity_Periods
    template_name = 'memberactivityapp/confirmdelete.html'
    success_url = '/'
    pk_url_kwarg = 'pk'

class ApiView(SerializeMixin,View):
    model = Members
    def get(self,*args,**kwargs):
        
        qs = self.serialize(*args,**kwargs)
        return JsonResponse(qs,safe=False)

