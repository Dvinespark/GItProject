from django.conf.urls import url
from .import views


urlpatterns =[

    url(r'^$',views.Index, name='index'),
    url(r'^$',views.user_register, name='register'),
    url(r'^my_cv$',views.my_cv, name='my_cv'),


]