# Generated by Django 2.1.15 on 2022-12-07 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0002_auto_20221207_1354'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=50)),
                ('found_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='accounts/avatar/blank_profile.png', upload_to='accounts/avatar')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Company')),
                ('friends', models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='register.UserProfile')),
                ('project', models.ManyToManyField(blank=True, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='invite',
            name='invited',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_invites', to='register.UserProfile'),
        ),
        migrations.AddField(
            model_name='invite',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='made_invites', to='register.UserProfile'),
        ),
    ]
