# Generated by Django 5.0.6 on 2024-06-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title2', models.CharField(blank=True, default='Site Title 2', max_length=100)),
            ],
            options={
                'verbose_name': 'preferences2',
                'verbose_name_plural': 'preferences2',
            },
        ),
        migrations.AlterModelOptions(
            name='preferences',
            options={'verbose_name': 'preferences', 'verbose_name_plural': 'preferences'},
        ),
    ]
