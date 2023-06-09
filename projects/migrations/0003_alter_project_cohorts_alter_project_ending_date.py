# Generated by Django 4.0 on 2023-05-22 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
        ('projects', '0002_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cohorts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dash.cohorts'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ending_date',
            field=models.DateField(auto_created=True),
        ),
    ]
