# Generated by Django 2.2.2 on 2019-06-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancetype',
            name='summary',
            field=models.TextField(default='Summary ..'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='insurancetype',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
