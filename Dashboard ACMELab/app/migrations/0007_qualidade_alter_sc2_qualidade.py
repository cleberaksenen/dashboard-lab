# Generated by Django 5.0.4 on 2024-06-22 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_redcapsc2_sc2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='sc2',
            name='qualidade',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='SC2_qua', to='app.qualidade'),
        ),
    ]