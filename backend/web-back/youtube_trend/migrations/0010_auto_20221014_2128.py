# Generated by Django 3.0.5 on 2022-10-14 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_trend', '0009_auto_20221014_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrankdata',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='youtube_trend.VideoData'),
        ),
    ]