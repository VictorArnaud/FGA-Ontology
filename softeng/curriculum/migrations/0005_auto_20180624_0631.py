# Generated by Django 2.0.6 on 2018-06-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_multidiciplinary_fixture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='credits',
            field=models.PositiveIntegerField(help_text='Discipline credits', verbose_name='Credits'),
        ),
    ]
