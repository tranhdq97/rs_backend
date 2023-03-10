# Generated by Django 4.1.5 on 2023-01-24 12:53

import base.common.constant.db_table
import base.common.models.base
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('is_available', models.BooleanField(verbose_name=True)),
                ('created_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_created_by', to='staff.staff')),
                ('updated_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_updated_by', to='staff.staff')),
            ],
            options={
                'db_table': base.common.constant.db_table.DBTable['TABLE'],
            },
        ),
    ]
