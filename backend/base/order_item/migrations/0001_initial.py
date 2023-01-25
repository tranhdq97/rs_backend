# Generated by Django 4.1.5 on 2023-01-24 12:58

import base.common.constant.db_table
import base.common.models.base
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('menu', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('served_quantity', models.IntegerField(default=0)),
                ('served_at', models.DateTimeField(null=True)),
                ('created_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_created_by', to='staff.staff')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['MENU'], to='menu.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['ORDER_ITEM'], to='order.order')),
                ('updated_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_updated_by', to='staff.staff')),
            ],
            options={
                'db_table': base.common.constant.db_table.DBTable['ORDER_ITEM'],
            },
        ),
    ]
