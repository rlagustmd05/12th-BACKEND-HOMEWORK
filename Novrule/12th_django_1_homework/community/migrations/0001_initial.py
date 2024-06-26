# Generated by Django 4.2.11 on 2024-04-09 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.user')),
            ],
        ),
    ]
