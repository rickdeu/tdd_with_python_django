# Generated by Django 4.1.2 on 2022-10-28 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_alter_item_lista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='lista',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.list'),
        ),
    ]
