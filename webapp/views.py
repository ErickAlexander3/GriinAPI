from django.shortcuts import render
import pdb

# Create your views here.
def home(request):

	pdb.set_trace()
	
	return render(request, 'home.html')