# Generated by Django 2.0.1 on 2020-12-10 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textApp', '0013_auto_20201210_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookchapter',
            name='chapter_types',
            field=models.CharField(choices=[(1, '免费'), (2, '会员')], default=2, max_length=5),
        ),
    ]