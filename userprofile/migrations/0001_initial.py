# Generated by Django 4.0 on 2023-04-23 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('local_govt', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=200)),
                ('contact_add', models.CharField(max_length=600)),
                ('courses', models.CharField(max_length=300)),
                ('laptop', models.CharField(max_length=200)),
                ('certifcate', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('social_media', models.CharField(max_length=200)),
                ('social_medialink', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('rejected', 'rejected'), ('admitted', 'admitted')], default='pending', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.myuser')),
            ],
        ),
    ]