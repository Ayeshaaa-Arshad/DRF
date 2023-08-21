# Generated by Django 4.2.4 on 2023-08-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(
                    decimal_places=3, default=0.0, max_digits=20)),
            ],
        ),
    ]
