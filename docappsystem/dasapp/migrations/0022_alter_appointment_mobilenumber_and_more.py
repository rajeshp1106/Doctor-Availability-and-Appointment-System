# Generated by Django 5.0.7 on 2024-07-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0021_remove_appointment_timeslot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='mobilenumber',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin')], default=2, max_length=50),
        ),
    ]
