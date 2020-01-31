# Generated by Django 2.2.9 on 2020-01-30 21:32

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'applications',
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300, unique=True, verbose_name='title')),
                ('is_open', models.BooleanField(default=True, verbose_name='are applications open')),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('courts_number', models.IntegerField(verbose_name='courts number')),
                ('schedule_system', models.CharField(choices=[('8', '8 Teams system'), ('16', '16 Teams system'), ('32', '32 Team system')], default='16', max_length=2, verbose_name='Schedule by number of teams participated')),
                ('type', models.CharField(choices=[('Beach', 'Beach Volleyball'), ('4X4', '4X4 Volleyball')], default='4X4', max_length=40, verbose_name='Type of competition')),
                ('gender', models.CharField(choices=[('w', 'Woman'), ('m', 'Man'), ('x', 'Mixes')], default='m', max_length=1, verbose_name='gender')),
            ],
            options={
                'db_table': 'competition',
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('place', models.IntegerField(null=True, verbose_name='place')),
                ('ranking', models.IntegerField(verbose_name='ranking points')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.Competition', verbose_name='competition')),
            ],
            options={
                'db_table': 'rankings',
            },
        ),
    ]
