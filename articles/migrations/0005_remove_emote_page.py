# Generated by Django 3.2.18 on 2023-04-28 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_emote_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emote',
            name='page',
        ),
    ]