from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from django.utils.timesince import timesince
from apps.report.models import ReportForm, Report
from django.conf import settings
from django.views.generic import TemplateView, FormView
from apps.report.forms import Report2Form
from django.core.urlresolvers import reverse_lazy
from unipath import Path


def index(request):
	form=ReportForm()
	reports=Report.objects.all().order_by('-fecha')
	return render_to_response('report/index.html',{'form': form, 'msg':reports}, context_instance=RequestContext(request))

def report_save(request):	
	if request.is_ajax():
		form = ReportForm(request.POST)
		if form.is_valid():
			form.save()
			reports=Report.objects.all().order_by('-fecha')
			data='<ul>'
			for report in reports:
				data +='<li> %s %s %s %s Hace %s</li>' %(report.tag, report.nombre, report.descripcion, report.user, timesince(report.fecha))
			data+='</ul>'
			return HttpResponse(json.dumps({'ok':True,'msg':data }), mimetype='application/json')
		else:
			return HttpResponse(json.dumps({'ok':False,'msg':'Debes llenar los campos.'}), mimetype='application/json')

class index2(FormView):
	template_name ='report/index.html'
	form_class=Report2Form
	success_url = reverse_lazy('index2')
#	reports=Report.objects.all().order_by('-fecha')
#	data='<ul>'
#	for report in reports:
#		data +='<li> %s %s %s %s Hace %s</li>' %(report.tag, report.nombre, report.descripcion, report.user, timesince(report.fecha))
#		data+='</ul>'
#		return HttpResponse(json.dumps({'ok':True,'msg':data }), mimetype='application/json')
#	else:
#		return HttpResponse(json.dumps({'ok':False,'msg':'Debes llenar los campos.'}), mimetype='application/json')

	

# from django.shortcuts import render_to_response
# from django.views.generic import TemplateView

# def index(request):
# 	return render_to_response('report/index.html')

# class index2(TemplateView):
# 	template_name = 'report/index.html'

class ReportSave(TemplateView):	

	def post(self, request, *args, **kwargs):
		print request.method		
		if request.is_ajax():		
			print request.POST	
			print request.FILES			
			form = Report2Form(data=request.POST)
			form.imagenes = request.POST[u'imagenes']
			print request.POST[u'imagenes']
			print form.imagenes
			#print form.errors
			#print form
			if form.is_valid():
				report1= Report()
				print report1

				report1.tag=form.cleaned_data['tag']
				report1.nombre=form.cleaned_data['nombre']
				report1.descripcion=form.cleaned_data['descripcion']
				report1.lng=form.cleaned_data['lng']
				report1.lat=form.cleaned_data['lat']				
				report1.user=form.cleaned_data['user']
				archivo=form.cleaned_data['imagenes']
				report1.imagenes=form.cleaned_data['imagenes']
				pfile=Path(settings.MEDIA_ROOT, str(archivo))
				
				print pfile #isfile()				
				report1.save()
				pfile.remove()
				reports=Report.objects.all().order_by('-fecha')
				data='<ul>'
				for report in reports:
					for field in report._meta.fields:
						print field.name						
						print report.fecha
					print type(report)
					#data +='<li> %s %s %s %s Hace %s</li>' %(report.tag, report.nombre, report.descripcion, report.user, timesince(report.fecha))
				data+='</ul>'
				return HttpResponse(json.dumps({'ok':True,'msg':data }), content_type='application/json')
			else:
				return HttpResponse(json.dumps({'ok':False,'msg':'Debes llenar los campos.'}), content_type='application/json')
