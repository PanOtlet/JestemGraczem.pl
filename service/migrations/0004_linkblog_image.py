# Generated by Django 2.0.6 on 2018-07-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_linkblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkblog',
            name='image',
            field=models.URLField(null=True, verbose_name='Miniatura'),
        ),
    ]