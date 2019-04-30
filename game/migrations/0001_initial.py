# Generated by Django 2.2 on 2019-04-30 13:54

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
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lvl', models.IntegerField(default=0)),
                ('bonus', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BuildingType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField()),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('time_to_recruit', models.FloatField()),
                ('speed', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('deffence', models.IntegerField()),
                ('loot', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('points', models.IntegerField()),
                ('map_x', models.IntegerField()),
                ('map_y', models.IntegerField()),
                ('morale', models.IntegerField(default=100)),
                ('owned_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VillageResource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Resource')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Village')),
            ],
        ),
        migrations.CreateModel(
            name='VillageResearch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Research')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Village')),
            ],
        ),
        migrations.CreateModel(
            name='VillageArmy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Unit')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Village')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceUnitCost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resource_cost', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.ResourceCost')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceBuildingCost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Building')),
                ('resource_cost', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.ResourceCost')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('building_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.BuildingType')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='building_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.BuildingInfo'),
        ),
        migrations.AddField(
            model_name='building',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Village'),
        ),
    ]
