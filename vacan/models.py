from django.db import models
from vacancies.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE, related_name='vacancies', default=None,
                                   null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies', default=None,
                                null=True, blank=True)
    skills = models.CharField(max_length=128)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
    application = models.ForeignKey('application.Application', on_delete=models.CASCADE, related_name='vacancies', default=None,
                                    null=True, blank=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='vacancies', default=None,
                              null=True, blank=True)


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True)
    location = models.CharField(max_length=32, blank=True)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, blank=True)
    desc = models.TextField(blank=True)
    employee_count = models.IntegerField(blank=True, null=True)


class Speciality(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=32)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR, blank=True)


