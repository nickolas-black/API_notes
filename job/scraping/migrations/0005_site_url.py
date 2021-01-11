from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_auto_20210108_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Сайт для поиска')),
            ],
            options={
                'verbose_name_plural': 'Сайты для поиска',
                'verbose_name': 'Сайт для поиска',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_address', models.CharField(max_length=250, unique=True, verbose_name='Адрес для поиска')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='Город')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Site', verbose_name='Сайт для поиска')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Specialty', verbose_name='Специальность')),
            ],
            options={
                'verbose_name_plural': 'Адресы для поиска',
                'verbose_name': 'Адрес для поиска',
            },
        ),
    ]
