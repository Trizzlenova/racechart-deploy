# Generated by Django 2.1.1 on 2018-09-06 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('birth_place', models.CharField(max_length=500)),
                ('birthday', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('car_number', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(max_length=1)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=500, null=True)),
                ('driver_id', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('residence', models.CharField(blank=True, max_length=200, null=True)),
                ('rookie_year', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('actual_distance', models.FloatField(blank=True, null=True)),
                ('avg_speed', models.FloatField(blank=True, null=True)),
                ('caution_laps', models.IntegerField(blank=True, null=True)),
                ('cautions', models.CharField(blank=True, max_length=250, null=True)),
                ('condition', models.CharField(blank=True, max_length=250, null=True)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('elapsed_time', models.CharField(blank=True, max_length=250, null=True)),
                ('flags', models.IntegerField(blank=True, null=True)),
                ('laps', models.IntegerField(blank=True, null=True)),
                ('laps_completed', models.IntegerField(blank=True, null=True)),
                ('lead_changes', models.IntegerField(blank=True, null=True)),
                ('race_number', models.IntegerField(blank=True, null=True)),
                ('scheduled_time', models.DateTimeField(blank=True, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('track', models.CharField(blank=True, max_length=250, null=True)),
                ('victory_margin', models.FloatField(blank=True, null=True)),
                ('drivers', models.ManyToManyField(related_name='races', to='racechart_app.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_position', models.FloatField(blank=True, null=True)),
                ('avg_speed', models.FloatField(blank=True, null=True)),
                ('best_lap', models.IntegerField(blank=True, null=True)),
                ('best_lap_speed', models.FloatField(blank=True, null=True)),
                ('best_lap_time', models.FloatField(blank=True, null=True)),
                ('bonus_points', models.IntegerField(blank=True, null=True)),
                ('driver_rating', models.FloatField(blank=True, null=True)),
                ('elapsed_time', models.FloatField(blank=True, null=True)),
                ('fastest_laps', models.IntegerField(blank=True, null=True)),
                ('laps_completed', models.IntegerField(blank=True, null=True)),
                ('laps_led', models.IntegerField(blank=True, null=True)),
                ('passes_made', models.IntegerField(blank=True, null=True)),
                ('passing_differential', models.IntegerField(blank=True, null=True)),
                ('penalty_points', models.IntegerField(blank=True, null=True)),
                ('pit_stops', models.IntegerField(blank=True, null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('quality_passes', models.IntegerField(blank=True, null=True)),
                ('start_position', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('times_led', models.IntegerField(blank=True, null=True)),
                ('times_passed', models.IntegerField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='racechart_app.Driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='racechart_app.Race')),
            ],
        ),
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_finish_position', models.FloatField(blank=True, null=True)),
                ('avg_laps_completed', models.FloatField(blank=True, null=True)),
                ('avg_start_postion', models.FloatField(blank=True, null=True)),
                ('chase_bonus', models.IntegerField()),
                ('dnf', models.IntegerField(blank=True, null=True)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('in_chase', models.BooleanField()),
                ('laps_completed', models.IntegerField(blank=True, null=True)),
                ('laps_led', models.IntegerField(blank=True, null=True)),
                ('laps_led_pct', models.IntegerField(blank=True, null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('poles', models.IntegerField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('stage_wins', models.IntegerField(blank=True, null=True)),
                ('starts', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=200)),
                ('top_5', models.IntegerField(blank=True, null=True)),
                ('top_10', models.IntegerField(blank=True, null=True)),
                ('top_15', models.IntegerField(blank=True, null=True)),
                ('top_20', models.IntegerField(blank=True, null=True)),
                ('wins', models.IntegerField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standings', to='racechart_app.Driver')),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('crew_chief', models.CharField(blank=True, max_length=1000, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=1000, null=True)),
                ('sponsors', models.CharField(blank=True, max_length=1000, null=True)),
                ('owner', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='racechart_app.Team'),
        ),
    ]
