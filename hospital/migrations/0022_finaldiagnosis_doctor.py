# Generated by Django 3.1 on 2024-11-10 05:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_diagnosis_diagnosis_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='finaldiagnosis',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.doctor'),
            preserve_default=False,
        ),
    ]
