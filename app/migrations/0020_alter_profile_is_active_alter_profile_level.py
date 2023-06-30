# Generated by Django 4.2 on 2023-04-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_profile_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('admin', 'Administrator'), ('casher', 'Kassir'), ('teacher', "O'qituvchi"), ('null', 'Lavozim mavjud emas')], default='null', max_length=10),
        ),
    ]