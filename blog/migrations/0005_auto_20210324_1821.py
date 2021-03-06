# Generated by Django 3.1.1 on 2021-03-24 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210324_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user_blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog_user'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog_user'),
        ),
    ]
