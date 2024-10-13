# Generated by Django 3.1 on 2024-06-08 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_kh', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tbl_building',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_no', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.building')),
            ],
            options={
                'db_table': 'tbl_floor',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20)),
                ('service_charge', models.FloatField()),
                ('price', models.FloatField()),
                ('room_key', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('note', models.CharField(max_length=100)),
                ('floor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.floor')),
                ('room_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.roomtype')),
            ],
            options={
                'db_table': 'tbl_room',
            },
        ),
    ]
