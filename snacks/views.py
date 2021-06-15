from django.urls.base import reverse_lazy
from snacks.models import Snack
from django.db import models
from django.shortcuts import render
from django.utils.translation import templatize
from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView,
    DetailView, 
    UpdateView,
    DeleteView 
    )

# Create your views here.


## Home View
class SnackView(TemplateView):
    template_name = "home.html"
    model = Snack

## List View 
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

## Create View
class SnackCreatView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title", "purchaser", "description"]

## Detail View
class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

## Update View
class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title", "description"]

## Delete View
class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")


