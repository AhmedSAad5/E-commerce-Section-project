# Generated by Django 4.0.4 on 2022-05-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-id',)},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='active',
            new_name='is_active',
        ),
    ]
