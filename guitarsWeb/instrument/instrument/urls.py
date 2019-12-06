"""instrument URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import InstrumentCreateView, InstrumentListView, MyInstrumentListView, InstrumentDetailView, InstrumentUpdateView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('instrument/user/', MyInstrumentListView.as_view(), name='myinstruments'),
    path('instrument/list/', InstrumentListView.as_view(), name="instrument-list"),
    path('instrument/detail/<int:pk>/', InstrumentDetailView.as_view(), name='instrument-detail'),
    path('instrument/register/', InstrumentCreateView.as_view(), name='instrument-register'),
    path('instrument/edit/<int:pk>/', InstrumentUpdateView.as_view(), name='instrument-edit'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login'))),
    path('', RedirectView.as_view(url='instrument/list/'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)