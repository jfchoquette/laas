# Generated by Django 2.2 on 2023-07-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_userprofile_ipa_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ipa_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]