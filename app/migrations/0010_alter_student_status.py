# Generated by Django 4.2 on 2023-04-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_student_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('0', "O'chirilgan"), ('1', 'Aktiv')], default='1', max_length=15),
        ),
    ]
