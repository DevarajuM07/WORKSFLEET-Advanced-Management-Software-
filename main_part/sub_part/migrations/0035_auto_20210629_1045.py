# Generated by Django 3.2.3 on 2021-06-29 05:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0034_auto_20210629_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='manage_expense',
            name='plate',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manage_expense',
            name='vehicle_model',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manage_income',
            name='total_amount',
            field=models.CharField(max_length=100),
        ),
    ]
