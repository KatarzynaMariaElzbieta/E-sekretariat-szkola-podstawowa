# Generated by Django 2.2.7 on 2020-05-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_office', '0002_recruit_school_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='flat_number',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
