# Generated by Django 5.0.7 on 2024-08-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0006_remove_asettings_add_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adname', models.CharField(max_length=100)),
                ('addlogo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
