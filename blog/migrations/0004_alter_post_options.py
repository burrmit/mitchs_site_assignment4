# Generated by Django 4.1.1 on 2022-10-03 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_weirdstuff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]
