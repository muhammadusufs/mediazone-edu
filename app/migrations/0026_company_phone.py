# Generated by Django 4.2 on 2023-04-22 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_group_company_subscription_company_teacher_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
