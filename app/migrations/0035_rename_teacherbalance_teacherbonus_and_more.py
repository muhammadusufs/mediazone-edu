# Generated by Django 4.2 on 2023-04-24 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_teacherbalancehistory_teacherbalance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeacherBalance',
            new_name='TeacherBonus',
        ),
        migrations.RenameModel(
            old_name='TeacherBalanceHistory',
            new_name='TeacherBonusHistory',
        ),
    ]
