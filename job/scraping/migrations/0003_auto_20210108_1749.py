
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_vacancy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='Город'),
        ),
    ]
