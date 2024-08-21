"""
URL configuration for MatatuFinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from M3FinderApp.views import HomeView, TransportationLocationView, EnterDestinationView, search_destinations, ContactUsView, SuccessView
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('enter_destination/', EnterDestinationView.as_view(), name='enter_destination'),
    path('transportation_location/', TransportationLocationView.as_view(), name='transportation_location'),
    path('search_destinations/', search_destinations, name='search_destinations'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('success/', SuccessView.as_view(), name='success'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
