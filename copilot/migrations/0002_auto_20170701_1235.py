# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('copilot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, serialize=False, related_name='copilot_eventlist', to='cms.CMSPlugin')),
                ('artist_id', models.UUIDField(null=True, verbose_name='artist id', blank=True)),
                ('event_count', models.PositiveIntegerField(help_text='The maximum number of events to show.', verbose_name='number of events', default=5, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='news',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, serialize=False, related_name='copilot_news', to='cms.CMSPlugin'),
        ),
    ]
