# Generated by Django 4.0.1 on 2022-04-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dep_name', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('resume', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]
