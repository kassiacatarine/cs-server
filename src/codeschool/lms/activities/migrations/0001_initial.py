# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 00:51
from __future__ import unicode_literals

import decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import wagtail.contrib.wagtailroutablepage.models
import wagtail_model_tools.models.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityList',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('short_description', models.CharField(help_text='A short textual description to be used in titles, lists, etc.', max_length=140, verbose_name='short description')),
            ],
            options={
                'verbose_name': 'list of activities',
                'verbose_name_plural': 'lists of activities',
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ActivitySection',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('short_description', models.CharField(help_text='A short textual description to be used in titles, lists, etc.', max_length=140, verbose_name='short description')),
                ('material_icon', models.CharField(default='help', max_length=20, verbose_name='Optional icon')),
            ],
            options={
                'verbose_name': 'section',
                'verbose_name_plural': 'sections',
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('opened', 'opened'), ('closed', 'closed')], default='opened', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('final_score', models.DecimalField(decimal_places=3, default=decimal.Decimal, help_text='Final grade given to considering all submissions, penalties, etc.', max_digits=6, verbose_name='final score')),
                ('given_grade', models.DecimalField(decimal_places=3, default=decimal.Decimal, help_text='Final grade before applying any modifier.', max_digits=6, verbose_name='grade')),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('points', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('stars', models.FloatField(default=0.0)),
                ('is_correct', models.BooleanField(default=bool)),
                ('has_submissions', models.BooleanField(default=bool)),
                ('has_feedback', models.BooleanField(default=bool)),
                ('has_post_tests', models.BooleanField(default=bool)),
                ('activity_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'student progress',
                'verbose_name_plural': 'student progress list',
            },
            bases=(wagtail_model_tools.models.mixins.CopyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('pending', 'pending'), ('incomplete', 'incomplete'), ('waiting', 'waiting'), ('invalid', 'invalid'), ('done', 'done')], default='pending', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('hash', models.CharField(blank=True, max_length=32)),
                ('ip_address', models.CharField(blank=True, max_length=20)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_activities.submission_set+', to='contenttypes.ContentType')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='activities.Progress')),
            ],
            options={
                'verbose_name': 'submission',
                'verbose_name_plural': 'submissions',
            },
            bases=(wagtail_model_tools.models.mixins.CopyMixin, models.Model),
        ),
        migrations.AddField(
            model_name='progress',
            name='best_submission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='activities.Submission'),
        ),
        migrations.AddField(
            model_name='progress',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_activities.progress_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='progress',
            unique_together=set([('user', 'activity_page')]),
        ),
    ]
