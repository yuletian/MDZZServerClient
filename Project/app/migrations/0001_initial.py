# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 03:04
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
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='BW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Boss')),
            ],
        ),
        migrations.CreateModel(
            name='KeFu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Boss')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation', models.CharField(max_length=50)),
                ('kefu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.KeFu')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Worker'),
        ),
        migrations.AddField(
            model_name='bw',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Worker'),
        ),
    ]
