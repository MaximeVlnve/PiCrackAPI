# Generated by Django 3.1.2 on 2020-10-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='network',
            name='password',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
