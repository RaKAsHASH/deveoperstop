# Generated by Django 3.2.5 on 2022-07-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220728_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='mailmail@mail.com', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='AAAA', max_length=200),
            preserve_default=False,
        ),
    ]
