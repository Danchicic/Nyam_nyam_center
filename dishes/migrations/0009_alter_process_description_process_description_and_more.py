# Generated by Django 5.0.3 on 2024-03-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0008_remove_process_description_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_description',
            name='process_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='process_description',
            name='time',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
