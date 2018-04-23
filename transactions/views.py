# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Transaction
from properties.models import Property


class PropertyTransactionListView(generic.ListView):
    """Lists the transactions associated with a property object. """

    model = Transaction
    template_name = 'transactions/list.html'

    def get_queryset(self, **kwargs):
        prop = self.kwargs.get('prop_pk')
        return Transaction.objects.filter(prop__pk=prop)

    def get_context_data(self, **kwargs):
        context = super(PropertyTransactionListView, self).get_context_data(**kwargs)
        context['prop'] = Property.objects.get(pk=self.kwargs.get('prop_pk'))
        return context



# Begin lab 10 modifications below...