# Generated by Django 4.2 on 2023-04-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_subscription_student_alter_student_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='cost',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='cost',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
