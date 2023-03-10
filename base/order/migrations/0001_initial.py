# Generated by Django 4.1.5 on 2023-01-24 12:57

import base.common.constant.db_table
import base.common.models.base
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('table', '0001_initial'),
        ('staff', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('num_people', models.IntegerField()),
                ('paid_at', models.DateTimeField(null=True)),
                ('created_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_created_by', to='staff.staff')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['CUSTOMER'], to='customer.customer')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['ORDER'], to='table.table')),
                ('updated_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_updated_by', to='staff.staff')),
            ],
            options={
                'db_table': base.common.constant.db_table.DBTable['ORDER'],
            },
        ),
    ]
