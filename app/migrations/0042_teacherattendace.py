# Generated by Django 4.2 on 2023-04-26 05:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_profile_barcode_alter_expense_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherAttendace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.profile')),
            ],
        ),
    ]
