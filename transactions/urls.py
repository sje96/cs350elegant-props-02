# transactions/urls.py

from django.conf.urls import url

from . import views

app_name = 'transactions'

urlpatterns = [
    url(r'^list/(?P<prop_pk>[0-9]+)/$', views.PropertyTransactionListView.as_view(), name='list_by_prop'),
]