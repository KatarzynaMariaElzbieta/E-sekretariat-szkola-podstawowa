# Generated by Django 2.2.7 on 2020-05-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_office', '0006_auto_20200530_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='further_information',
            field=models.TextField(null=True, verbose_name='Dodatkowe informacje'),
        ),
    ]
