from django.db import models


class PCManager(models.Manager):
    def get_pc_by_processor_id(self, id):
        return self.filter(id_processor=id).all()


class Processor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=False)
    frequency = models.IntegerField()
    memory_cash = models.IntegerField()

    class Meta:
        db_table = 'processor'


class PC(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=False)
    price = models.IntegerField()
    id_processor = models.ForeignKey('Processor', models.DO_NOTHING, db_column='id_processor', blank=True, null=True)

    objects = PCManager()

    class Meta:
        db_table = 'pc'
