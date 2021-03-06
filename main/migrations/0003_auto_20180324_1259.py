# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-24 12:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20180324_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_agent', models.BooleanField(default=False)),
                ('referer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='agent',
            name='user',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='Investor',
        ),
    ]
