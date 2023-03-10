# Generated by Django 4.1.6 on 2023-02-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(default='Name of service...', max_length=200)),
                ('service_description', models.TextField(default='Describe service...')),
            ],
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
