"""vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from vacan.views import MainView, VacanciesListView, CategoriesListView,  VacancyView, CompanyView # ResumeSenderView, CompanyListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('companies/<int:comp_id>/', CompanyView.as_view(), name='company'),
    path('jobs/cat/<str:spec_id>/', CategoriesListView.as_view(), name='category'),
    path('jobs/<int:vac_id>/', VacancyView.as_view(), name='onevacancy'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)