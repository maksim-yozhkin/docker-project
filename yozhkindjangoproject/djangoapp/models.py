from django.db import models

class Brigades(models.Model):
    number_brigade = models.AutoField(primary_key=True)
    number_phone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'brigades'


class Locomotives(models.Model):
    reg_number = models.AutoField(primary_key=True)
    reg_depo = models.CharField(max_length=10)
    type = models.CharField(max_length=30)
    year_prod = models.DateField()

    class Meta:
        managed = False
        db_table = 'locomotives'


class Repairs(models.Model):
    code = models.AutoField(primary_key=True)
    reg_num_loc = models.ForeignKey(Locomotives, models.DO_NOTHING, db_column='reg_num_loc', blank=True, null=True)
    type = models.CharField(max_length=30)
    date_start = models.DateField()
    needed_days = models.IntegerField()
    cost_one_day = models.TextField()
    number_brigade = models.ForeignKey(Brigades, models.DO_NOTHING, db_column='number_brigade', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repairs'


class Workers(models.Model):
    code_worker = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=20)
    number_brigade = models.ForeignKey(Brigades, models.DO_NOTHING, db_column='number_brigade', blank=True, null=True)
    brigadier = models.BooleanField()
    date_birth = models.DateField()

    class Meta:
        managed = False
        db_table = 'workers'