# Generated by Django 4.0.3 on 2022-10-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_yazilar'),
    ]

    operations = [
        migrations.AddField(
            model_name='yazilar',
            name='yazi_path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
