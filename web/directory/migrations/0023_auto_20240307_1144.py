# Generated by Django 3.2.24 on 2024-03-07 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0022_alter_coopaddresstags_coop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=165)),
                ('state', models.CharField(max_length=8)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(default='US', max_length=2)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.AlterField(
            model_name='coopaddresstags',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.address'),
        ),
    ]