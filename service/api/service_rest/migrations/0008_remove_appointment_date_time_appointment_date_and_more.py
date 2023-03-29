# Generated by Django 4.0.3 on 2023-01-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0007_alter_appointment_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
