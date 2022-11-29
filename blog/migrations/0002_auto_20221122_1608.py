# Generated by Django 2.0.13 on 2022-11-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fCode', models.IntegerField()),
                ('fTitle', models.CharField(max_length=50)),
                ('fTopic', models.CharField(max_length=50)),
                ('fWriter', models.CharField(max_length=50)),
                ('fDesc', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='facinfo',
            old_name='fcode',
            new_name='fCode',
        ),
    ]