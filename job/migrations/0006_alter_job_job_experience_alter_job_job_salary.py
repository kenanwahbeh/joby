# Generated by Django 5.0.6 on 2024-06-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_job_experience_job_job_salary_job_job_vacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
