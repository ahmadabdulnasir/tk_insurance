# Generated by Django 2.2.2 on 2019-06-13 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_auto_20190613_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='insurance_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.InsuranceType'),
        ),
    ]
