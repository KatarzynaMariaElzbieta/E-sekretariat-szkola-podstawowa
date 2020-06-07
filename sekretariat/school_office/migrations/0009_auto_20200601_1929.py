# Generated by Django 2.2.7 on 2020-06-01 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_office', '0008_auto_20200531_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruit',
            name='catchment_area',
        ),
        migrations.AddField(
            model_name='recruit',
            name='no_catchment_area',
            field=models.BooleanField(default=False, verbose_name='Spoza obwodu szkoły'),
        ),
        migrations.AlterField(
            model_name='nocatchmentareainformation',
            name='siblings_info',
            field=models.TextField(null=True, verbose_name='Rodzeństwo (imię, nazwisko, rok urodzenia)'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_date', models.DateField(auto_now=True)),
                ('application_content', models.TextField()),
                ('attachment', models.FileField(upload_to='')),
                ('type', models.IntegerField(choices=[(1, 'rekrutacja'), (2, 'legitymacja'), (3, 'karta rowerowa'), (4, 'świetlica')])),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_office.Recruit')),
            ],
        ),
    ]
