# Generated by Django 3.2.8 on 2021-10-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essays', '0006_essay_essay_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='uuid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]