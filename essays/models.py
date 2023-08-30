from django.db import models

# Create your models here.

class Essay(models.Model):
    student_name = models.CharField(db_column="student_name", max_length=100)
    student_no = models.IntegerField(db_column="student_number")
    subject = models.CharField(max_length=100, db_column="subject", blank=True, null=True); 
    secondary_subject = models.CharField(max_length=100, db_column="secondary_subject", blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    essay_type = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    context = models.TextField(db_column="context")
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    uuid = models.CharField(max_length=100,  blank=True, null=True); 

    def __str__(self):
        return "%s %d号 %s %s" % (self.category, self.student_no, self.student_name, self.subject)
    
    def context_p(self):
        co = self.context.replace('<', '&lt;').replace('>', '&gt;')
        return "<p class='indent'>"+co.replace('\n',"</p><p class='indent'>")+"</p>"
    
