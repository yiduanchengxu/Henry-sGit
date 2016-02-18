# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160217_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='timetamp',
            new_name='timestamp',
        ),
    ]
