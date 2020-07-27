# Generated by Django 3.0.8 on 2020-07-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='award1',
            field=models.IntegerField(blank=True, choices=[(1, 'tomato_basil_spaghetti'), (2, 'tomato_lasagna'), (3, 'tomato_pizza'), (4, 'tomato_sauce_penne'), (5, 'tomato_sauce_spaghetti')], null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='award2',
            field=models.IntegerField(blank=True, choices=[(1, 'tomato_basil_spaghetti'), (2, 'tomato_lasagna'), (3, 'tomato_pizza'), (4, 'tomato_sauce_penne'), (5, 'tomato_sauce_spaghetti')], null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='award3',
            field=models.IntegerField(blank=True, choices=[(1, 'tomato_basil_spaghetti'), (2, 'tomato_lasagna'), (3, 'tomato_pizza'), (4, 'tomato_sauce_penne'), (5, 'tomato_sauce_spaghetti')], null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='award4',
            field=models.IntegerField(blank=True, choices=[(1, 'tomato_basil_spaghetti'), (2, 'tomato_lasagna'), (3, 'tomato_pizza'), (4, 'tomato_sauce_penne'), (5, 'tomato_sauce_spaghetti')], null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='award5',
            field=models.IntegerField(blank=True, choices=[(1, 'tomato_basil_spaghetti'), (2, 'tomato_lasagna'), (3, 'tomato_pizza'), (4, 'tomato_sauce_penne'), (5, 'tomato_sauce_spaghetti')], null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='award_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='plant1_stage',
            field=models.IntegerField(choices=[(1, 'seed'), (2, 'plant_stage2'), (3, 'plant_stage3'), (4, 'plant_stage4'), (5, 'plant_stage5'), (6, 'plant_stage6'), (7, 'plant_stage7')], default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='plant2_stage',
            field=models.IntegerField(choices=[(1, 'seed'), (2, 'plant_stage2'), (3, 'plant_stage3'), (4, 'plant_stage4'), (5, 'plant_stage5'), (6, 'plant_stage6'), (7, 'plant_stage7')], default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='plant3_stage',
            field=models.IntegerField(choices=[(1, 'seed'), (2, 'plant_stage2'), (3, 'plant_stage3'), (4, 'plant_stage4'), (5, 'plant_stage5'), (6, 'plant_stage6'), (7, 'plant_stage7')], default=1),
        ),
    ]
