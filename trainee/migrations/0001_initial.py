# Generated by Django 5.1.6 on 2025-03-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username_field', models.CharField(db_column='username ', max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.BigIntegerField()),
            ],
            options={
                'db_table': 'trainee',
                'managed': False,
            },
        ),
    ]
