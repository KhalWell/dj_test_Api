# Generated by Django 4.2.1 on 2023-05-31 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=150, verbose_name='last name')),
                ('father_name', models.CharField(blank=True, max_length=150, verbose_name='Father name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='fake_path')),
                ('pay', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old', models.PositiveSmallIntegerField()),
                ('current_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.department')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='admin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.employee'),
        ),
    ]