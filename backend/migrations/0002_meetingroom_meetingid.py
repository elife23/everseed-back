# Generated by Django 4.2.5 on 2023-10-04 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingroom',
            name='meetingid',
            field=models.ForeignKey(db_column='meetingId', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='backend.meeting'),
        ),
    ]
