from django.db import models

# Create your models here.
class Resume(models.Model):
    # Организация выбора в поле статуса
    NOT_LOOKING_FOR_WORK = 'NLW'
    LOOKING_FOR_WORK = 'LW'
    CONSIDERING_OFFERS = 'CO'
    STATUS_CHOICES = [
        (NOT_LOOKING_FOR_WORK, "Не ищу работу"),
        (LOOKING_FOR_WORK, "Ищу работу"),
        (CONSIDERING_OFFERS, "Рассматриваю предложения"),
    ]
    # Организация выбора в поле уровня
    INTERN = 'IN'
    JUNIOR = 'JR'
    MIDDLE = 'ML'
    SENIOR = 'SR'
    LEAD = 'LD'
    GRADE_CHOICES = [
        (INTERN, "Стажер"),
        (JUNIOR, "Джуниор"),
        (MIDDLE, "Миддл"),
        (SENIOR, "Синьор"),
        (LEAD, "Лид"),
    ]
    # Организация выбора в поле образования
    BACHELOR = 'BL'
    ENGINEER = 'IN'
    MASTER = 'MR'
    PHD = 'PH'
    DOCTOR = 'DR'
    NO_EDUCATION = 'NG'
    EDUCATION_CHOICES = [
        (BACHELOR, "Бакалавриат"),
        (ENGINEER, "Специалитет"),
        (MASTER, "Магистратура"),
        (PHD, "Кандидат наук"),
        (DOCTOR, "Доктор наук"),
        (NO_EDUCATION, "Нет специального образования, но богатый опыт"),
    ]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='resumes', default=None, null=True,
                             blank=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=LOOKING_FOR_WORK)
    salary = models.IntegerField()
    specialty = models.ForeignKey('vacan.Speciality', on_delete=models.CASCADE, related_name='resumes', default=None,
                                  null=True, blank=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default=JUNIOR)
    education = models.CharField(max_length=2, choices=EDUCATION_CHOICES, default=ENGINEER)
    experience = models.IntegerField()
    portfolio = models.TextField()