# Generated by Django 3.2.4 on 2021-06-11 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20210611_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='create_at',
        ),
        migrations.AddField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='criado_em'),
            preserve_default=False,
        ),
    ]
