# Generated by Django 3.2.16 on 2023-02-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_alter_family_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educational_bg',
            name='c_graduation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='educational_bg',
            name='d_graduation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='educational_bg',
            name='e_graduation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='educational_bg',
            name='h_graduation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='educational_bg',
            name='m_graduation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employment_info',
            name='date_hired',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='license',
            name='exam_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='birthdate',
            field=models.DateField(),
        ),
    ]