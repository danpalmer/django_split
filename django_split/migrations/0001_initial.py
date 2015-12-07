# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 11:51
from __future__ import unicode_literals

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
            name='ExperimentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment', models.CharField(max_length=48)),
                ('group', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='django_split_experiment_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment', models.CharField(max_length=48)),
                ('group', models.IntegerField()),
                ('metric', models.IntegerField()),
                ('percentile', models.IntegerField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentState',
            fields=[
                ('experiment', models.CharField(max_length=48, primary_key=True, serialize=False)),
                ('started', models.DateTimeField(null=True)),
                ('completed', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='experimentresult',
            unique_together=set([('experiment', 'group', 'metric', 'percentile')]),
        ),
        migrations.AlterUniqueTogether(
            name='experimentgroup',
            unique_together=set([('experiment', 'user')]),
        ),
    ]
