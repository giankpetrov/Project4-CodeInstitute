"""
URL configuration for project4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
import reservations.views
import members.views


urlpatterns = [
    path('', reservations.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('reservations/', reservations.views.reservations,
         name='reservations'),
    path('update_reservation/<reservation_id>',
         reservations.views.update_reservation,
         name='update-reservation'),
    path('create_reservation/',
         reservations.views.create_reservation,
         name='create-reservation'),
    path('delete_reservation/<reservation_id>',
         reservations.views.delete_reservation,
         name='delete-reservation'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    # path('reservations/', include('reservations.urls')),
]
