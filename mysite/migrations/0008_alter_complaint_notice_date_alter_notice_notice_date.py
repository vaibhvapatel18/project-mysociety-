# Generated by Django 4.1.4 on 2022-12-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='notice_date',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_date',
            field=models.CharField(max_length=25),
        ),
    ]