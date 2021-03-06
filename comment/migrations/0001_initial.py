# Generated by Django 3.1.1 on 2021-03-25 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0010_auto_20210326_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('on_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog_user')),
            ],
        ),
    ]
