# Generated by Django 3.2.11 on 2022-03-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220331_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]