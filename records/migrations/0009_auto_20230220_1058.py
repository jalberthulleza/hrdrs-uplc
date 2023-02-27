# Generated by Django 3.2.16 on 2023-02-20 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_alter_family_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address1',
            name='user',
        ),
        migrations.RemoveField(
            model_name='educational_bg',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employment_info',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personal_info',
            name='family',
        ),
        migrations.RemoveField(
            model_name='personal_info',
            name='license',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.AlterField(
            model_name='family',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='f_account', to='records.personal_info'),
        ),
        migrations.AlterField(
            model_name='license',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='l_account', to='records.personal_info'),
        ),
    ]