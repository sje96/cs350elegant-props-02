# transactions/urls.py

from django.conf.urls import url

from . import views

app_name = 'transactions'

urlpatterns = [
    url(r'^list/(?P<prop_pk>[0-9]+)/$', views.PropertyTransactionListView.as_view(), name='list_by_prop'),
    url(r'^(?P<pk>[0-9]+)/$',views.PropertyTransactionDetailView.as_view(),name='detail'),
    url(r'^add/$', views.PropertyCreateTransaction.as_view(), name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.PropertyUpdateTransaction.as_view(), name='edit'),
]