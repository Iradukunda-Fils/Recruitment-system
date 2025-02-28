# Generated by Django 5.1.2 on 2024-10-29 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0014_alter_branch_branch_image_alter_company_logo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('job_level', models.CharField(choices=[('entry', 'Entry Level'), ('mid', 'Mid-Senior Level'), ('senior', 'Senior Level')], max_length=10)),
                ('job_function', models.CharField(max_length=50)),
                ('employment_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract'), ('internship', 'Internship')], max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('education', models.CharField(choices=[('no_degree', 'No Degree'), ('o_level', 'O Level'), ('high_school', 'High School Diploma'), ('bachelors', 'Bachelor’s Degree'), ('masters', 'Master’s Degree'), ('phd', 'PhD or Doctorate')], max_length=20)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('application_deadline', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='companies.company')),
            ],
        ),
    ]
