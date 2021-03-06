# Generated by Django 2.1.4 on 2019-01-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='describe',
            field=models.CharField(max_length=100, null=True, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='category',
            name='fid',
            field=models.CharField(max_length=20, null=True, verbose_name='父节点'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(max_length=20, null=True, verbose_name='关键字'),
        ),
    ]
