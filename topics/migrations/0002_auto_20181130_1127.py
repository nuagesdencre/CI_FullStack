# Generated by Django 2.1.3 on 2018-11-30 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topicfollower',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='topics.Topic'),
        ),
    ]