# Generated by Django 5.1.4 on 2024-12-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('specialization', models.CharField(max_length=20)),
                ('experience', models.IntegerField()),
                ('address', models.TextField()),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
