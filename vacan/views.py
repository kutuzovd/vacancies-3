from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.db.models import Count
from vacan.models import Vacancy, Company, Speciality
# Create your views here.

#Обработчик главной страницы (аннотирование по специализациям и компаниям)
class MainView(View):
    def get(self, request):
        specialty_vacancies = Speciality.objects.annotate(count_speciality=Count('vacancies'))
        company_vacancies = Company.objects.annotate(count_company=Count('vacancies'))
        return render(request, 'index.html', context={'specialty_vacancies': specialty_vacancies,
                                                      'company_vacancies': company_vacancies})


#Обработчик показа листа всех вакансий
class VacanciesListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        title_page = 'Все вакансии'
        return render(request, 'list.html', context={'vacancies' : vacancies,
                                                     'title_page' : title_page })


#Обработчик показа листа вакансий по категориям
class CategoriesListView(View):
    def get(self, request, spec_id):
        vacancies = Vacancy.objects.filter(speciality__code=spec_id).all()
        title_page = Speciality.objects.filter(code=spec_id).first().title
        return render(request, 'list.html', context={'vacancies' : vacancies,
                                                     'title_page' : title_page})


#Обработчик показа одной вакансии
class VacancyView(View):
    def get(self, request, vac_id):
        vacancy = Vacancy.objects.filter(id=vac_id).first()
        return render(request, 'vacancy.html', context={'vacancy' : vacancy})


#Обработчик показа вакансий одной компании
class CompanyView(View):
    def get(self, request, comp_id):
        company = Company.objects.filter(id=comp_id).first()
        vacancies = Vacancy.objects.filter(company__id=comp_id).all()
        return render(request, 'company.html', context={'company' : company,
                                                        'vacancies' : vacancies})
