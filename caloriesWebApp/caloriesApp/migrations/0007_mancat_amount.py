# Generated by Django 4.0 on 2021-12-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caloriesApp', '0006_remove_mancat_articole_mancate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mancat',
            name='amount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9),
        ),
    ]