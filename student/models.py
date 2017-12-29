from django.db import models

class Teacher(models.Model):
    tno = models.CharField(primary_key=True, max_length=4)
    tname = models.CharField(max_length=8, blank=True, null=True)
    title = models.CharField(max_length=10, blank=True, null=True)

    #class Meta:
        #managed = True   #False
        #db_table = 'teacher'

    def __str__(self):
        return self.tno+self.tname
		
class Student(models.Model):
    sno = models.CharField(primary_key=True, max_length=4)
    sname = models.CharField(max_length=8, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)

    #class Meta:
        #managed = True   #False
        #db_table = 'student'
    
    def __str__(self):
        return self.sno+self.sname
    
class Course(models.Model):
    cno = models.CharField(primary_key=True, max_length=4)
    cname = models.CharField(max_length=20, blank=True, null=True)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='tno', blank=True, null=True)

    #class Meta:
        #managed = True   #False
        #db_table = 'course'
    
    def __str__(self):
        return self.cno+self.cname

class Sc(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='sno')
    course = models.ForeignKey('Course', models.DO_NOTHING, db_column='cno')
    score = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        #managed = True   #False
        #db_table = 'sc'
        unique_together = (('student', 'course'),)

    def __str__(self):
        return '/'.join([self.student_id,self.student.sname,self.course_id,self.course.cname,self.course.teacher.tname,repr(self.score)])


