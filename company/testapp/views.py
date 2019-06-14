from django.shortcuts import render
from testapp.models import company
fro django.views.generic import ListView,DetailView,UpdateView
from djnago.core.urlresolvers import reverse_lazy
# Create your views here.
class companylist(ListView):
    model=company

class companydetail(DetailView):
    model=company

class companyupdateview(UpdteView):
    model=company
    fields=('name','ceo','city')

class companycreateview(CreateView):
    model=company
    fields=('name','ceo','city')

class companydeleteview(DeleteView):
    model=company1
    success_url=reverse_lazy('company')
