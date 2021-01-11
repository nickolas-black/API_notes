from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0007_auto_20210108_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='legal_words',
            field=models.CharField(blank=True, max_length=250, verbose_name='Название специальности, для проверки совпадений'),
        ),
    ]
