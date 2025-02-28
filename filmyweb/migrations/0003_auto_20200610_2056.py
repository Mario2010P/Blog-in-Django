# Generated by Django 3.0.7 on 2020-06-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0002_auto_20200610_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='opis',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='film',
            name='plakat',
            field=models.ImageField(blank=True, null=True, upload_to='plakaty'),
        ),
        migrations.AddField(
            model_name='film',
            name='premiera',
            field=models.DateField(blank=True, null=True),
        ),
    ]
