# Generated by Django 4.2.4 on 2023-08-09 14:59

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("feed", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
    ]
