# Generated by Django 3.2.16 on 2023-02-17 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0006_auto_20230217_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='education', to='records.educational_bg'),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='employment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employment', to='records.employment_info'),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='family',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='family', to='records.family'),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='license', to='records.license'),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='records.question'),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
    ]
