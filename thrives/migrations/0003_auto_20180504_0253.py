# Generated by Django 2.0.4 on 2018-05-04 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thrives', '0002_auto_20180422_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='thrive',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='thrives', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='thrive',
            name='story',
            field=models.TextField(),
        ),
    ]
