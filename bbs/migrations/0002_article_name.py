# Generated by Django 4.0.1 on 2022-02-02 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
