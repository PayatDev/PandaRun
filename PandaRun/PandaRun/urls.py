"""PandaRun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from webapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^result/', views.result, name='result'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^FQA/', views.FQA, name='FQA'),
    url(r'^reward/', views.reward, name='reward'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^course/', views.course, name='course'),
    url(r'^regis_info/', views.regis_info, name='regis_info'),
    url(r'^register/', views.register, name='register'),
    url(r'^full_regis/', views.full_regis, name='full_regis'),
    url(r'^half_regis/', views.half_regis, name='half_regis'),
    url(r'^check/', views.check, name='check'),
    url(r'^contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
