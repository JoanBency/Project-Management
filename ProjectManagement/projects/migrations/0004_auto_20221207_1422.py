# Generated by Django 2.1.15 on 2022-12-07 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20221207_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='company',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='register.Company'),
        ),
    ]
