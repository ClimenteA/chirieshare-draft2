# Generated by Django 3.0.1 on 2020-01-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200119_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anunt',
            name='numar_colegi',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
