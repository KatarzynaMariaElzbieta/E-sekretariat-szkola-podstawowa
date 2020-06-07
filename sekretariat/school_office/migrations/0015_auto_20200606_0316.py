# Generated by Django 2.2.7 on 2020-06-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_office', '0014_application_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_content',
            field=models.TextField(verbose_name='Treść'),
        ),
        migrations.AlterField(
            model_name='application',
            name='attachment',
            field=models.FileField(null=True, upload_to='app_attachment_directory_path', verbose_name='Załączniki'),
        ),
        migrations.AlterField(
            model_name='application',
            name='type',
            field=models.IntegerField(choices=[(1, 'PODANIE REKRUTACYJNE'), (2, 'PODANIE O LEGITYMACJĘ'), (3, 'PODANIE O KARTĘ ROWEROWĄ'), (4, 'PODANIE O ZAPIS NA ŚWIETLICĘ')], verbose_name='Typ podania'),
        ),
    ]
