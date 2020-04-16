from django.db import models

# Create your models here.
class Application(models.Model):
    written_username = models.CharField(max_length=32)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField(blank=True)
    vacancy = models.ForeignKey('vacan.Vacancy', on_delete=models.CASCADE, related_name='applications', default=None,
                                null=True, blank=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='applications', default=None,
                             null=True, blank=True)