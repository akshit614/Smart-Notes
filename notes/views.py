from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes
from django.views.generic import DeleteView,UpdateView,ListView,DetailView,CreateView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


# Create your views here.

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = '/smart/notes/'
    template_name = 'notes/notes_delete.html'
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()



class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm
    login_url = "/login"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        
    



class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()

class NoteDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()

    




