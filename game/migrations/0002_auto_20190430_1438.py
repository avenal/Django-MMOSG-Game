# Generated by Django 2.2 on 2019-04-30 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VillageBuilding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lvl', models.IntegerField(default=0)),
                ('bonus', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='building',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='building',
            name='building_info',
        ),
        migrations.RemoveField(
            model_name='building',
            name='lvl',
        ),
        migrations.RemoveField(
            model_name='building',
            name='village',
        ),
        migrations.AddField(
            model_name='building',
            name='building_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='game.BuildingType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='building',
            name='name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BuildingInfo',
        ),
        migrations.AddField(
            model_name='villagebuilding',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Building'),
        ),
        migrations.AddField(
            model_name='villagebuilding',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Village'),
        ),
    ]