# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'', max_length=1000)),
                ('author', models.ForeignKey(to='forum.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'', max_length=1000)),
                ('author', models.ForeignKey(to='forum.Student')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=b'', max_length=1000),
        ),
    ]
