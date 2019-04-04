from django.shortcuts import render

from portfolio.models import AnalogProject
from portfolio.models import DigitalProject

def portfolio_index(request):

	analog_projects = AnalogProject.objects.all()
	digital_projects = DigitalProject.objects.all()

	context = {
		'analog_projects': analog_projects,
		'digital_projects': digital_projects,
	}
	
	return render(request, 'portfolio/portfolio.html', context)