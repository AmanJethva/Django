# Generated by Django 4.0.4 on 2022-06-08 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexapp', '0004_alter_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=100)),
                ('email', models.CharField(default=0, max_length=100)),
                ('password', models.CharField(default=0, max_length=100)),
                ('cname', models.CharField(default=0, max_length=100)),
            ],
        ),
    ]
