# Generated by Django 2.0 on 2020-12-05 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textApp', '0003_auto_20201205_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookchapter',
            name='books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter_book', to='textApp.Books', verbose_name='小说名'),
        ),
    ]
