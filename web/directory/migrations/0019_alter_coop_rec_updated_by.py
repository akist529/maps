# Generated by Django 3.2.24 on 2024-02-24 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory', '0018_auto_20240224_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coop',
            name='rec_updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]