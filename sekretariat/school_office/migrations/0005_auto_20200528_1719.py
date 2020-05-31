# Generated by Django 2.2.7 on 2020-05-28 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_office', '0004_auto_20200527_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='approval',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_office.Approval'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='school_class',
            field=models.IntegerField(choices=[(0, 'Oddział 0'), (1, 'Klasa I'), (2, 'Klasa II'), (3, 'Klasa III'), (4, 'Klasa IV'), (5, 'Klasa V'), (6, 'Klasa VI'), (7, 'Klasa VII'), (8, 'Klasa VIII')], default=0, verbose_name='Klasa'),
        ),
    ]