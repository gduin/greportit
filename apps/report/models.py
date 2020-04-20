# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Report(models.Model):
	tag         = models.CharField('Etiqueta', max_length=50)
	nombre      = models.CharField('Nombre', max_length=50)
	descripcion = models.CharField('Descripcion', max_length=250)
	imagenes    = models.FileField(upload_to='User', blank=True, null=True, max_length=255)
	fecha       = models.DateTimeField(auto_now=True)
	#fecha1		= models.DateTimeField(auto_now_add=True,auto_now=True)
	lat         = models.CharField(max_length=50)
	lng         = models.CharField(max_length=50)
	user        = models.ForeignKey(User)


	def __unicode__(self):
		return self.tag
    #class Meta:
	#	verbose_name        = _('Report')
	#	verbose_name_plural = _('Reports')

    #def __unicode__(self):
    #    return self.tag

# class Tag(object):
# 	nombre = models.CharField('Tag', max_length=50)
# 	report = models.ManyToManyField(Report)

# 	def __unicode__(self):
# 		return self.nombre
		
class ReportForm(ModelForm):
    class Meta:
        model = Report
