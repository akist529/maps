# Generated by Django 3.0 on 2020-06-11 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_contactmethod_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coop',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_email', to='directory.ContactMethod'),
        ),
        migrations.AlterField(
            model_name='coop',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_phone', to='directory.ContactMethod'),
        ),
        migrations.AlterUniqueTogether(
            name='contactmethod',
            unique_together={('phone', 'email')},
        ),
    ]