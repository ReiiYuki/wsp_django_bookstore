from django.conf.urls import url

from . import views

app_name = 'book'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^insert/$',views.insert_book,name='insert'),
    url(r'^delete/$',views.delete_book,name='delete'),
    url(r'^update/$',views.update_book,name='update'),
    url(r'^request/update/$',views.update_request,name='update_request')
]
