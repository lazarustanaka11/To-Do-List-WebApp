# Generated by Django 3.2.8 on 2021-10-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20211017_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]