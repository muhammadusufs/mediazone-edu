# Generated by Django 4.2 on 2023-04-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_profile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
            preserve_default=False,
        ),
    ]
