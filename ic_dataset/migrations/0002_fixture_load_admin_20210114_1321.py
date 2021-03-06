# Generated by Django 3.0.8 on 2021-01-14 13:21
import os
from sys import path
from django.core import serializers
from django.db import migrations


fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'default_admin_dump.json'

def load_fixture(apps, schema_editor):

    fixture_file = os.path.join(fixture_dir, fixture_filename)

    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()
    fixture.close()


# def unload_fixture(apps, schema_editor):
#     "Brutally deleting all entries for this model..."
#
#     MyModel = apps.get_model("yourapp", "ModelName")
#     MyModel.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('ic_dataset', '0001_initial'),
    ]

    operations = [
        # migrations.RunPython(load_fixture, reverse_code=unload_fixture),
        migrations.RunPython(load_fixture),
    ]


