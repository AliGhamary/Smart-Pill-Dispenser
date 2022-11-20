# Generated by Django 4.1.3 on 2022-11-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_pills_pill'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='hour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pill',
            name='minute',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pill',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
