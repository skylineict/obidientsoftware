# Generated by Django 4.0 on 2023-05-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_end_date_alter_project_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='end_date',
            new_name='ending_date',
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]