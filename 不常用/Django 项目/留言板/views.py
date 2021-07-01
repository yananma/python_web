from django.shortcuts import render
import pysnooper
from .forms import ContactForm
from .models import Contact
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponseRedirect

# Create your views here.

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'

class ContactView(FormView):
    contact_name = 'contact.html'
    form_class = ContactForm

class ContactCreate(CreateView):
    model = Contact
    fields = ['name', 'email', 'content', 'category']
    success_url = '/myapp/list'
    template_name = 'contact.html'


class ContactUpdate(UpdateView):
    template_name = 'contact_update.html'
    model = Contact
    fields = ['name', 'email', 'content', 'category']
    success_url = '/myapp/list'


class ContactDelete(DeleteView):
    model = Contact
    success_url = '/myapp/list'
    template_name = 'contact_confirm_delete.html'

