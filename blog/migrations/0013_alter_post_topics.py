# Generated by Django 4.1.1 on 2022-10-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_created_alter_post_topics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(related_name='blog_posts', to='blog.topic'),
        ),
    ]