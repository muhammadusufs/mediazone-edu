# Generated by Django 4.2 on 2023-04-24 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_rename_teacherbalance_teacherbonus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherbonus',
            name='balance_history',
        ),
        migrations.AddField(
            model_name='teacherbonus',
            name='comment',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TeacherBonusHistory',
        ),
    ]
