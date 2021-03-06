# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Source1.ExitQ1_AttribQuote'
        db.add_column('mydata_source1', 'ExitQ1_AttribQuote',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ2_PhotoPermit'
        db.add_column('mydata_source1', 'ExitQ2_PhotoPermit',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ3_ClassReDo'
        db.add_column('mydata_source1', 'ExitQ3_ClassReDo',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ4_ExamPrep'
        db.add_column('mydata_source1', 'ExitQ4_ExamPrep',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ5_GroupStudy'
        db.add_column('mydata_source1', 'ExitQ5_GroupStudy',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ6_ExpectedGrade'
        db.add_column('mydata_source1', 'ExitQ6_ExpectedGrade',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ7_EcoachFrequency'
        db.add_column('mydata_source1', 'ExitQ7_EcoachFrequency',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ8_PrimaryUse'
        db.add_column('mydata_source1', 'ExitQ8_PrimaryUse',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ9_GoodBadFeatures'
        db.add_column('mydata_source1', 'ExitQ9_GoodBadFeatures',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ExitQ10_Misc'
        db.add_column('mydata_source1', 'ExitQ10_Misc',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Exit_Q11_SurveyTimes'
        db.add_column('mydata_source1', 'Exit_Q11_SurveyTimes',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Source1.ExitQ1_AttribQuote'
        db.delete_column('mydata_source1', 'ExitQ1_AttribQuote')

        # Deleting field 'Source1.ExitQ2_PhotoPermit'
        db.delete_column('mydata_source1', 'ExitQ2_PhotoPermit')

        # Deleting field 'Source1.ExitQ3_ClassReDo'
        db.delete_column('mydata_source1', 'ExitQ3_ClassReDo')

        # Deleting field 'Source1.ExitQ4_ExamPrep'
        db.delete_column('mydata_source1', 'ExitQ4_ExamPrep')

        # Deleting field 'Source1.ExitQ5_GroupStudy'
        db.delete_column('mydata_source1', 'ExitQ5_GroupStudy')

        # Deleting field 'Source1.ExitQ6_ExpectedGrade'
        db.delete_column('mydata_source1', 'ExitQ6_ExpectedGrade')

        # Deleting field 'Source1.ExitQ7_EcoachFrequency'
        db.delete_column('mydata_source1', 'ExitQ7_EcoachFrequency')

        # Deleting field 'Source1.ExitQ8_PrimaryUse'
        db.delete_column('mydata_source1', 'ExitQ8_PrimaryUse')

        # Deleting field 'Source1.ExitQ9_GoodBadFeatures'
        db.delete_column('mydata_source1', 'ExitQ9_GoodBadFeatures')

        # Deleting field 'Source1.ExitQ10_Misc'
        db.delete_column('mydata_source1', 'ExitQ10_Misc')

        # Deleting field 'Source1.Exit_Q11_SurveyTimes'
        db.delete_column('mydata_source1', 'Exit_Q11_SurveyTimes')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mydata8.common1': {
            'BirthDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'BirthMo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'BirthYr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Class_Standing': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'College': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'College_Other': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Concentrate_Other': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology_EEB': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology_MCDB': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Chemistry': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Education': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Engineering': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Health': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Humanities': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__IDK': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Math': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Neurosci': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Other': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Physics': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Psych_BBCS': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Social_Science_not_Psych': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Stats': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Cum_GPA_Survey': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Declared': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'Employment': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'First_Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'High_School_CumGPA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Greek': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Music_Art': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Other': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Religious': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Research': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Sports': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Volunteering': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Last_Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Common1', 'db_table': "'mydata_common1'"},
            'Other_Commitment': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Parent_Ed': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'Post_College': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'Semesters_Completed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uniqname': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'mydata8.emptysource': {
            'Meta': {'object_name': 'EmptySource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'mydata8.source1': {
            'APCourses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'APCoursesTaken__Biology': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'APCoursesTaken__Chemistry': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'APCoursesTaken__Math': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'APCoursesTaken__Other': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'APCoursesTaken__Physics': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Attendance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Confidence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130DiscussionAttendance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Friends': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130GoalGrade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130GradeConfidence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130HoursStudy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Interest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130OWLHours': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Reason__Concentration_req': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Reason__Credit': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Reason__Grad_req': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Reason__Interest': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130Reason__Possible_Concentrate_req': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'CHEM130SLC': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ChemPrevious': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_1_Satisfaction': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_1_Score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Satisfaction': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ10_Misc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ1_AttribQuote': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ2_PhotoPermit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ3_ClassReDo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ4_ExamPrep': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ5_GroupStudy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ6_ExpectedGrade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ7_EcoachFrequency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ8_PrimaryUse': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ExitQ9_GoodBadFeatures': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Exit_Q11_SurveyTimes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Final_Exam_Score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_01__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_02__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_03__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_04__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_05__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_06__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_07__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_08__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_09__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_10__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_11__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_12__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_13__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_14__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_15__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Mat_Calculator': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Mat_Textbook': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Mat_iClicker': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Math_Confidence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Message_2_Q1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Message_2_Q2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Message_2_Q3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Message_3_Q1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Source1', 'db_table': "'mydata_source1'"},
            'OWL_Avg_Exam1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'OWL_Avg_Exam2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'OWL_Avg_Final': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'PR_ProblemsTried_Exam1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'PR_ProblemsTried_Exam2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Participation_Avg_Exam1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Participation_Avg_Exam2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Participation_Avg_Final': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Post_Exam2_Feelings__1': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Post_Exam2_Feelings__2': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Post_Exam2_Feelings__3': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Post_Exam2_Feelings__4': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Post_Exam2_Feelings__5': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Post_Exam2_Feelings__6': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'PreExam2_Q1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Quiz_Avg_Exam1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Quiz_Avg_Exam2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Quiz_Avg_Final': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Reg_Acad_Level': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Reg_Enrolled': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Reg_GPA': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Reg_Gender': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'Signup_Opt_Out': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass01': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass03': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass04': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass05': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass06': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass07': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass08': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass10': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass11': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass12': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass13': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass14': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass15': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass16': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass17': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass18': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass19': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass20': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass21': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass22': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass23': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass24': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass25': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass26': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass27': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass28': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass29': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass30': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass31': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass32': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass33': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass34': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass35': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass36': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass37': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass38': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass39': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass40': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass41': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass42': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass43': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass44': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass45': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass46': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass47': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass48': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass49': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'YClass50': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dist_ID': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'}),
            'zombi_1_write': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zombi_2_review': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zombi_2_write': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zombi_3_review': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zombi_3_rewrite': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zombi_3_write': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zombi_4_rewrite': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zombi_group': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mydata8']