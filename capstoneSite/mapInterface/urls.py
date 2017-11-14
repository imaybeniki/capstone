from django.conf.urls import url
from mapInterface import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^about/$', views.about, name='about'),
]