# Generated by Django 3.0.1 on 2020-01-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200103_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anunt',
            name='img2',
            field=models.ImageField(default='anunturi/placeholder.svg', upload_to='anunturi/'),
        ),
        migrations.AlterField(
            model_name='anunt',
            name='img3',
            field=models.ImageField(default='anunturi/placeholder.svg', upload_to='anunturi/'),
        ),
        migrations.AlterField(
            model_name='anunt',
            name='img4',
            field=models.ImageField(default='anunturi/placeholder.svg', upload_to='anunturi/'),
        ),
        migrations.AlterField(
            model_name='anunt',
            name='img5',
            field=models.ImageField(default='anunturi/placeholder.svg', upload_to='anunturi/'),
        ),
        migrations.AlterField(
            model_name='anunt',
            name='img6',
            field=models.ImageField(default='anunturi/placeholder.svg', upload_to='anunturi/'),
        ),
    ]
