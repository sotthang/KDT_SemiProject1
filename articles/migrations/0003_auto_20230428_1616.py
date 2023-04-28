# Generated by Django 3.2.18 on 2023-04-28 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20230428_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emote',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='emote',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.review'),
        ),
    ]
