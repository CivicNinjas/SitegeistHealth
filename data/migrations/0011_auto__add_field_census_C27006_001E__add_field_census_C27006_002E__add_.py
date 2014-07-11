# -*- coding: utf-8 -*-
# flake8: noqa
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Census.C27006_001E'
        db.add_column(u'data_census', 'C27006_001E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_002E'
        db.add_column(u'data_census', 'C27006_002E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_003E'
        db.add_column(u'data_census', 'C27006_003E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_004E'
        db.add_column(u'data_census', 'C27006_004E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_005E'
        db.add_column(u'data_census', 'C27006_005E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_006E'
        db.add_column(u'data_census', 'C27006_006E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_007E'
        db.add_column(u'data_census', 'C27006_007E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_008E'
        db.add_column(u'data_census', 'C27006_008E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_009E'
        db.add_column(u'data_census', 'C27006_009E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_010E'
        db.add_column(u'data_census', 'C27006_010E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_011E'
        db.add_column(u'data_census', 'C27006_011E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_012E'
        db.add_column(u'data_census', 'C27006_012E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_013E'
        db.add_column(u'data_census', 'C27006_013E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_014E'
        db.add_column(u'data_census', 'C27006_014E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_015E'
        db.add_column(u'data_census', 'C27006_015E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_016E'
        db.add_column(u'data_census', 'C27006_016E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_017E'
        db.add_column(u'data_census', 'C27006_017E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_018E'
        db.add_column(u'data_census', 'C27006_018E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_019E'
        db.add_column(u'data_census', 'C27006_019E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_020E'
        db.add_column(u'data_census', 'C27006_020E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.C27006_021E'
        db.add_column(u'data_census', 'C27006_021E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Census.C27006_001E'
        db.delete_column(u'data_census', 'C27006_001E')

        # Deleting field 'Census.C27006_002E'
        db.delete_column(u'data_census', 'C27006_002E')

        # Deleting field 'Census.C27006_003E'
        db.delete_column(u'data_census', 'C27006_003E')

        # Deleting field 'Census.C27006_004E'
        db.delete_column(u'data_census', 'C27006_004E')

        # Deleting field 'Census.C27006_005E'
        db.delete_column(u'data_census', 'C27006_005E')

        # Deleting field 'Census.C27006_006E'
        db.delete_column(u'data_census', 'C27006_006E')

        # Deleting field 'Census.C27006_007E'
        db.delete_column(u'data_census', 'C27006_007E')

        # Deleting field 'Census.C27006_008E'
        db.delete_column(u'data_census', 'C27006_008E')

        # Deleting field 'Census.C27006_009E'
        db.delete_column(u'data_census', 'C27006_009E')

        # Deleting field 'Census.C27006_010E'
        db.delete_column(u'data_census', 'C27006_010E')

        # Deleting field 'Census.C27006_011E'
        db.delete_column(u'data_census', 'C27006_011E')

        # Deleting field 'Census.C27006_012E'
        db.delete_column(u'data_census', 'C27006_012E')

        # Deleting field 'Census.C27006_013E'
        db.delete_column(u'data_census', 'C27006_013E')

        # Deleting field 'Census.C27006_014E'
        db.delete_column(u'data_census', 'C27006_014E')

        # Deleting field 'Census.C27006_015E'
        db.delete_column(u'data_census', 'C27006_015E')

        # Deleting field 'Census.C27006_016E'
        db.delete_column(u'data_census', 'C27006_016E')

        # Deleting field 'Census.C27006_017E'
        db.delete_column(u'data_census', 'C27006_017E')

        # Deleting field 'Census.C27006_018E'
        db.delete_column(u'data_census', 'C27006_018E')

        # Deleting field 'Census.C27006_019E'
        db.delete_column(u'data_census', 'C27006_019E')

        # Deleting field 'Census.C27006_020E'
        db.delete_column(u'data_census', 'C27006_020E')

        # Deleting field 'Census.C27006_021E'
        db.delete_column(u'data_census', 'C27006_021E')


    models = {
        u'boundaryservice.boundary': {
            'Meta': {'ordering': "('kind', 'display_name')", 'object_name': 'Boundary'},
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '4269', 'null': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'metadata': ('boundaryservice.fields.JSONField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '192', 'db_index': 'True'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boundaries'", 'to': u"orm['boundaryservice.BoundarySet']"}),
            'shape': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'simple_shape': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256'})
        },
        u'boundaryservice.boundaryset': {
            'Meta': {'ordering': "('name',)", 'object_name': 'BoundarySet'},
            'authority': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind_first': ('django.db.models.fields.BooleanField', [], {}),
            'last_updated': ('django.db.models.fields.DateField', [], {}),
            'metadata_fields': ('boundaryservice.fields.ListField', [], {'separator': "'|'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'singular': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256'})
        },
        'data.census': {
            'B01003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_050E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_051E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_052E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_053E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_054E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_055E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_056E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_057E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_058E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_059E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19058_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19058_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19058_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_050E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_051E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_052E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_053E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_054E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_055E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_056E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_057E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_058E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_059E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_060E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_061E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_062E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_063E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_064E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_065E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_066E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_067E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_068E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_069E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_070E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_071E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_072E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_073E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_074E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_075E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_076E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_077E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_078E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_079E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_080E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_081E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_082E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_083E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_084E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_085E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_086E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_087E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_088E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_089E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_090E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_091E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_092E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_093E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_094E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_095E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_096E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_097E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_098E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_099E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_100E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_101E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_102E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_103E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_104E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_105E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_106E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_107E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_108E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_109E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_110E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_111E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_112E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_113E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_114E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_115E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_116E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_117E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_118E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_119E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_120E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_121E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_122E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_123E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_124E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_125E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_126E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_127E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_128E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_129E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_130E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_131E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_132E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_133E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_134E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_135E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_136E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_137E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_138E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_139E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_140E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_141E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_142E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_143E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_144E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_145E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_146E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_147E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_148E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_149E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_150E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_151E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_152E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_153E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_154E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_155E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_156E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_157E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_158E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_159E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_160E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_161E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_162E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_163E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_164E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_165E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_166E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_167E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_168E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_169E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_170E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_171E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_172E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_173E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25048_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25048_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25048_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25052_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25052_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25052_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Census'},
            'boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boundaryservice.Boundary']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logical_num': ('django.db.models.fields.IntegerField', [], {}),
            'state_abbr': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'data.dartmouth': {
            'Meta': {'object_name': 'Dartmouth'},
            'boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boundaryservice.Boundary']", 'null': 'True', 'blank': 'True'}),
            'discharge_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'data.ers': {
            'Meta': {'object_name': 'Ers'},
            'adult_diabetes': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'adult_obesity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boundaryservice.Boundary']", 'null': 'True', 'blank': 'True'}),
            'farmers_markets_per_thousand': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fast_food_rest_per_thousand': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'full_rest_per_thousand': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'grocery_stores_per_thousand': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent_low_access_to_groceries': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'percent_students_for_free_lunch': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'percent_students_for_reduced_lunch': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rec_facilities_per_thousand': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'state_abbr': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['data']
