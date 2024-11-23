# Generated by Django 5.1.3 on 2024-11-23 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.PositiveIntegerField(db_index=True, default=0, verbose_name='ordering')),
            ],
            options={
                'ordering': ['ordering'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parent2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parent3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parent4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('_orderaaaaa', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['_orderaaaaa'],
            },
        ),
        migrations.CreateModel(
            name='Child1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.PositiveIntegerField(db_index=True, default=0, verbose_name='ordering')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='testapp.parent1')),
            ],
            options={
                'ordering': ['ordering'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Child2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children+', to='testapp.parent2')),
            ],
        ),
        migrations.CreateModel(
            name='Child3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.parent3')),
            ],
        ),
    ]