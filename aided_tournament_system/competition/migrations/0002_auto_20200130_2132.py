# Generated by Django 2.2.9 on 2020-01-30 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0001_initial'),
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rankings', to='participant.Team', verbose_name='Team'),
        ),
        migrations.AddField(
            model_name='application',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='competition.Competition', verbose_name='competition'),
        ),
        migrations.AddField(
            model_name='application',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='participant.Team', verbose_name='Team'),
        ),
        migrations.AlterUniqueTogether(
            name='ranking',
            unique_together={('competition', 'team')},
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together={('team', 'competition')},
        ),
    ]
