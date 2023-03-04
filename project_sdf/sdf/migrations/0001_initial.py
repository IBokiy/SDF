# Generated by Django 4.1.7 on 2023-02-26 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=255, verbose_name='Title')),
                ('project_url', models.URLField(blank=True, verbose_name='URL')),
                ('project_type', models.CharField(choices=[('scrum', 'Scrum software development'), ('kanban', 'Kanban software development'), ('basic', 'Basic software development')], max_length=10, verbose_name='Type')),
                ('project_description', models.TextField(blank=True, verbose_name='Description')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Create date')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Update date')),
                ('project_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leading_projects', to=settings.AUTH_USER_MODEL, verbose_name='Lead')),
                ('project_members', models.ManyToManyField(blank=True, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Member')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
