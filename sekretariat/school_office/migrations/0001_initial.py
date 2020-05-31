# Generated by Django 2.2.7 on 2020-05-24 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.IntegerField(choices=[(1, 'Wielkopolskie'), (2, 'Kujawsko-pomorskie'), (3, 'Małopolskie'), (4, 'Łódzkie'), (5, 'Dolnośląskie'), (6, 'Lubelskie'), (7, 'Lubuskie'), (8, 'Mazowieckie'), (9, 'Opolskie'), (10, 'Podlaskie'), (11, 'Pomorskie'), (12, 'Śląskie'), (13, 'Podkarpackie'), (14, 'Świętokrzyskie'), (15, 'Warmińsko-Mazurskie'), (16, 'Zachodniopomorskie')])),
                ('county', models.CharField(max_length=64)),
                ('borough', models.CharField(max_length=64)),
                ('locality', models.CharField(max_length=64)),
                ('postcode', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('house_number', models.CharField(max_length=4)),
                ('flat_number', models.CharField(max_length=4)),
                ('phone_number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statutes', models.BooleanField()),
                ('data_updating', models.BooleanField()),
                ('nonconference', models.BooleanField()),
                ('religion', models.BooleanField()),
                ('photo_publication', models.BooleanField()),
                ('processing_of_personal_data', models.BooleanField()),
                ('provision', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('tel', models.IntegerField()),
                ('have_job', models.BooleanField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_office.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('PESEL', models.IntegerField(unique=True)),
                ('birthdate', models.DateField()),
                ('birthplace', models.CharField(max_length=64)),
                ('further_information', models.TextField()),
                ('catchment_area', models.BooleanField()),
                ('application_status', models.IntegerField(choices=[(1, 'oczekuje'), (2, 'rozpatrzony pozytywnie'), (3, 'odrzucony')])),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='father', to='school_office.Parent')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mother', to='school_office.Parent')),
                ('permanent_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permanent', to='school_office.Address')),
                ('residential_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residental', to='school_office.Address')),
            ],
        ),
        migrations.CreateModel(
            name='NoCatchmentAreaInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_family', models.BooleanField()),
                ('disabled', models.BooleanField()),
                ('siblings', models.BooleanField()),
                ('preschool', models.BooleanField()),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_office.Recruit')),
            ],
        ),
    ]