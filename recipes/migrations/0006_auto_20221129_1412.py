# Generated by Django 3.2.16 on 2022-11-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.CharField(default='0 mins', max_length=8),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.CharField(default='0 mins', max_length=8),
        ),
    ]
