# Generated by Django 3.2.16 on 2023-01-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='q10',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q10_details',
            field=models.CharField(default='Did?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q11',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q11_details',
            field=models.CharField(default='How?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q12',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q12_details',
            field=models.CharField(default='When?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q2_details',
            field=models.CharField(default='W?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q3_details',
            field=models.CharField(default='W?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q4_details',
            field=models.CharField(default='W?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q5_details',
            field=models.CharField(default='W?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q6',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q6_details',
            field=models.CharField(default='W?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q7',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q7_details',
            field=models.CharField(default='W?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q8',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q8_details',
            field=models.CharField(default='W?', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='q9',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q9_details',
            field=models.CharField(default='W?', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='q1_details',
            field=models.CharField(default='W?', max_length=100),
        ),
    ]
