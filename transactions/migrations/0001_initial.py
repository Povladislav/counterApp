# Generated by Django 4.1.3 on 2022-11-10 11:39

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_transaction', to='categories.category')),
            ],
        ),
    ]
