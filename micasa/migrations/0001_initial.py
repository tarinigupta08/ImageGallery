# Generated by Django 4.2.5 on 2023-09-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'upload',
                'verbose_name_plural': 'uploads',
            },
        ),
    ]
