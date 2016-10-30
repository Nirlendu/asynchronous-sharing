# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonPersonRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_follower_id', models.CharField(max_length=12)),
                ('person_followee_id', models.CharField(max_length=12)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonPrimary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15, unique=True)),
                ('person_name', models.CharField(max_length=30)),
                ('total_followers', models.IntegerField(default=0)),
                ('person_weight', models.DecimalField(decimal_places=10, default=0, max_digits=15)),
                ('person_created', models.DateTimeField(auto_now_add=True)),
                ('person_updated', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='personpersonrelation',
            unique_together=set([('person_follower_id', 'person_followee_id')]),
        ),
    ]