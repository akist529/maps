# Generated by Django 3.1.14 on 2023-08-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0014_auto_20230419_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='coops',
            field=models.ManyToManyField(related_name='people', to='directory.Coop'),
        ),
    ]
