# Generated by Django 4.0.6 on 2022-08-01 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
            options={
                'verbose_name': 'terrarium accessory',
                'verbose_name_plural': 'terrarium accessories',
            },
        ),
        migrations.CreateModel(
            name='Cricket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='sex')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('is_adult', models.BooleanField(blank=True, null=True, verbose_name='is adult')),
                ('wing_length', models.CharField(blank=True, choices=[('GT', 'Longer than forewings'), ('EQ', 'Same as forewings'), ('LT', 'Shorter than forewings')], max_length=2, verbose_name='hindwing length')),
                ('antenna_length', models.IntegerField(blank=True, null=True, verbose_name='antenna length')),
            ],
            options={
                'verbose_name': 'cricket',
                'verbose_name_plural': 'crickets',
            },
        ),
        migrations.CreateModel(
            name='CricketEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('type', models.CharField(choices=[('BIRTH', 'Birth'), ('DEATH', 'Death'), ('MOLT', 'Molt'), ('OTHER', 'Other')], max_length=5, verbose_name='event type')),
                ('event_date', models.DateField(blank=True, null=True, verbose_name='event date')),
                ('event_time', models.TimeField(blank=True, null=True, verbose_name='event time')),
                ('notes', models.TextField(blank=True, max_length=2000, verbose_name='notes')),
                ('cricket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='cricket.cricket', verbose_name='cricket')),
            ],
            options={
                'verbose_name': 'cricket event',
                'verbose_name_plural': 'cricket events',
            },
        ),
        migrations.CreateModel(
            name='Terrarium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='description')),
                ('accessories', models.ManyToManyField(related_name='terrariums', to='cricket.accessory', verbose_name='accessories')),
            ],
            options={
                'verbose_name': 'terrarium',
                'verbose_name_plural': 'terrariums',
            },
        ),
        migrations.CreateModel(
            name='CricketMolt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('becomes_adult', models.BooleanField(blank=True, null=True, verbose_name='becomes adult')),
                ('grows_wings', models.BooleanField(blank=True, null=True, verbose_name='grows wings')),
                ('grows_ovopositor', models.BooleanField(blank=True, null=True, verbose_name='grows ovopositor')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='molt', to='cricket.cricketevent', verbose_name='cricket molt')),
            ],
            options={
                'verbose_name': 'cricket molt',
                'verbose_name_plural': 'cricket molts',
            },
        ),
        migrations.AddField(
            model_name='cricket',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cricket.terrarium', verbose_name='location'),
        ),
    ]
