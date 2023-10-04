# Generated by Django 4.2.4 on 2023-10-04 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_book_readers_alter_book_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ok'), (2, 'Fine'), (3, 'Good'), (4, 'Amazing'), (5, 'Incredible')], null=True),
        ),
    ]
