# Generated by Django 3.2.16 on 2023-02-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_auto_20230220_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='validity_date',
            field=models.DateField(),
        ),
    ]