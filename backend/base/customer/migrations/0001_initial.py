# Generated by Django 4.1.5 on 2023-01-24 12:50

import base.common.constant.db_table
import base.common.models.base
import base.common.models.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_leave', models.BooleanField(default=False)),
                ('created_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_created_by', to='staff.staff')),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['CUSTOMER'], to='profile.profile')),
                ('updated_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_updated_by', to='staff.staff')),
            ],
            options={
                'db_table': base.common.constant.db_table.DBTable['CUSTOMER'],
            },
            managers=[
                ('objects', base.common.models.managers.CustomUserManager()),
            ],
        ),
    ]
