# Generated by Django 3.2.9 on 2022-02-21 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220221_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(help_text='form : 2022-10-25 14:30'),
        ),
    ]
