# Generated by Django 4.2.1 on 2023-09-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_diagnosis_alter_client_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='children',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Семейное положение, дети'),
        ),
        migrations.AlterField(
            model_name='client',
            name='life_events',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Жизненные события клиента'),
        ),
    ]
