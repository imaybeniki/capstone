from django.conf.urls import url
from mapInterface import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.profile, name='profile'),

    url(r'^ajax/get_points/$', views.get_points, name='get_points'),
    url(r'^ajax/update_user_points/$', views.update_user_points, name='update_user_points'),
]