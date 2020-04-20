from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from ajax_upload.widgets import AjaxClearableFileInput
from apps.report.models import Report

class Report2Form(ModelForm):

	def __init__(self, *args, **kwargs):
		super(Report2Form, self).__init__(*args, **kwargs)
		self.fields['imagenes'].required = False		


	class Meta:
		model = Report
		fields = ['tag', 'nombre', 'descripcion', 'imagenes', 'user', 'lat', 'lng']
		widgets ={
		'imagenes' : AjaxClearableFileInput,
		'lat': HiddenInput(),
		'lng': HiddenInput(),
		}    