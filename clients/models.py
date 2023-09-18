from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=20, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField()
    address = models.TextField(max_length=100, verbose_name='Адрес места жительства')
    education = models.TextField(max_length=100, verbose_name='Образование',blank=True, null=True)
    workplace = models.TextField(blank=True, null=True, max_length=100, verbose_name='Место работы')
    position = models.TextField(blank=True, null=True, max_length=100, verbose_name='Должность')
    children = models.TextField(blank=True, null=True, max_length=100, verbose_name='Семейное положение, дети')
    life_events = models.TextField(blank=True, null=True,max_length=100, verbose_name='Жизненные события клиента')
    illnesses = models.TextField(blank=True, null=True, verbose_name='Заболевания, жалобы клиента')
    diagnosis = models.TextField(blank=True, null=True, max_length=100, verbose_name='Диагноз')
    last_consultation_date = models.DateField(blank=True, null=True, verbose_name='Дата последней консультации')
    photo = models.ImageField(upload_to='clients/photos', blank=True, null=True)


    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
