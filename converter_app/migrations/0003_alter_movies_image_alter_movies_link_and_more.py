# Generated by Django 4.0.2 on 2022-02-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter_app', '0002_movies_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='link',
            field=models.URLField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
