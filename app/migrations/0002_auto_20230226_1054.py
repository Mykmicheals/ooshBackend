# Generated by Django 3.2 on 2023-02-26 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentclass',
            options={'verbose_name_plural': 'Student Class'},
        ),
        migrations.AlterModelOptions(
            name='studentdetails',
            options={'verbose_name_plural': 'Student Details'},
        ),
        migrations.RenameField(
            model_name='studentdetails',
            old_name='sex',
            new_name='gender',
        ),
    ]
