# Generated by Django 3.2.18 on 2023-05-02 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='article',
        ),
        migrations.CreateModel(
            name='ArticlePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.plan')),
            ],
        ),
    ]