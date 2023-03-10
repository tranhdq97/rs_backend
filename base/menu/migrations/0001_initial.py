# Generated by Django 4.1.5 on 2023-01-24 12:56

import base.common.constant.db_fields
import base.common.constant.db_table
import base.common.models.base
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file_management', '0001_initial'),
        ('staff', '0001_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('is_available', models.BooleanField(verbose_name=True)),
                ('created_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_created_by', to='staff.staff')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['MENU'], to='file_management.filemanagement')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['MENU'], to='master.mastermenutype')),
                ('updated_by', base.common.models.base.CurrentUserField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s_updated_by', to='staff.staff')),
            ],
            options={
                'db_table': base.common.constant.db_table.DBTable['MENU'],
                'unique_together': {(base.common.constant.db_fields.MenuFields['NAME'], base.common.constant.db_fields.MenuFields['TYPE_ID'])},
            },
        ),
    ]
