# Generated by Django 4.2 on 2023-04-22 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_group_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendace', models.BooleanField(default=False)),
                ('payment', models.BooleanField(default=False)),
                ('mark', models.BooleanField(default=False)),
                ('api_link', models.CharField(blank=True, max_length=280, null=True)),
                ('originator', models.CharField(blank=True, max_length=255, null=True)),
                ('key', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
    ]
