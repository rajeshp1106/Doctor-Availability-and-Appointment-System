# Generated by Django 5.0.7 on 2024-07-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0020_alter_appointment_date_of_appointment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='timeslot',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_of_appointment',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='prescription',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='recommendedtest',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='remark',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_of_appointment',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(upload_to='media/profile_pic'),
        ),
        migrations.AlterField(
            model_name='doctorreg',
            name='mobilenumber',
            field=models.CharField(max_length=15),
        ),
        migrations.DeleteModel(
            name='TimeSlot',
        ),
    ]
