# Generated by Django 5.0.1 on 2024-02-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_appointment_new_reports_newreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
