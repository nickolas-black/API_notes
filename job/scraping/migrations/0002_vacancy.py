from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250, unique=True, verbose_name='Адрес вакансии')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок вакансии')),
                ('description', models.TextField(blank=True, verbose_name='Описание вакансии')),
                ('company', models.CharField(blank=True, max_length=250, verbose_name='Название компании')),
                ('city', models.CharField(blank=True, max_length=250, verbose_name='Город')),
                ('speciality', models.CharField(blank=True, max_length=250, verbose_name='Специальность')),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
