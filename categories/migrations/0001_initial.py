# Generated by Django 4.1.3 on 2022-11-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_category', models.CharField(max_length=50, unique=True)),
                ('spent_sum', models.IntegerField(default=0)),
            ],
        ),
    ]
