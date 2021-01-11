from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_auto_20210108_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='speciality',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='specialty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scraping.Specialty', verbose_name='Специальность'),
            preserve_default=False,
        ),
    ]
