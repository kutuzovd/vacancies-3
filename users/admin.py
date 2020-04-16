from django.contrib import admin

# Register your models here.
from vacan.models import Vacancy, Company, Speciality
from resume.models import Resume
from application.models import Application

class VacancyAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

class SpecialityAdmin(admin.ModelAdmin):
    pass

class ResumeAdmin(admin.ModelAdmin):
    pass

class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Application, ApplicationAdmin)