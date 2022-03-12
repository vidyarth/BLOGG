from dataclasses import fields
from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
# from blog.myblog.models import post
from .models import post
from .forms import postform
from django.urls import reverse_lazy
# Create your views here.

class homeview(ListView):
    model = post
    template_name = "home.html"

class articleview(DetailView):
    model = post
    template_name = "article.html"

class addpost(CreateView):
    model = post
    form_class = postform
    template_name = "add.html"

class updatepost(UpdateView):
    model = post
    template_name = "update.html"
    fields = ("title","body")

class deletepost(DeleteView):
    model = post
    template_name = "delete.html"
    success_url = reverse_lazy('home')