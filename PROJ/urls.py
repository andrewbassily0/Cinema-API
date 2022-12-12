"""PROJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path , include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests' , views.viewsets_guest)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/jsonresponsefrommodel/', views.fbv_list),
    path('rest/fbv/<int:pk>', views.fbv_pk),
    path('rest/Cbv_list/', views.Cbv_list.as_view()),
    path('rest/Cbv_pk/<int:pk>', views.Cbv_pk.as_view()),
    path('rest/mixins_list/', views.Mixins_list.as_view()),
    path('rest/mixins_pk/<int:pk>', views.mixins_pk.as_view()),
    path('rest/generics_list/', views.Generics_list.as_view()),
    path('rest/generics_pk/<int:pk>', views.Generics_pk.as_view()),
    path('rest/viewsets/', include(router.urls)),
    path('rest/movies/', views.movies),
    path('rest/newreservation/', views.new),
]
