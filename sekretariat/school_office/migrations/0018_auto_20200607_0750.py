# Generated by Django 2.2.7 on 2020-06-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_office', '0017_auto_20200606_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='type',
            field=models.IntegerField(choices=[(1, 'PODANIE REKRUTACYJNE'), (2, 'PODANIE O LEGITYMACJĘ'), (3, 'PODANIE O KARTĘ ROWEROWĄ'), (4, 'PODANIE O ZAPIS NA ŚWIETLICĘ'), (5, 'INNE PODANIE')], verbose_name='Typ podania'),
        ),
    ]
