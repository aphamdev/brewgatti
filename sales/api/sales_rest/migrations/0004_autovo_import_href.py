# Generated by Django 4.0.3 on 2023-01-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0003_autovo_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='autovo',
            name='import_href',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]