from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Recommendation

# Create your views here.
def index(request):
    if request.method == 'POST':
        return recommendationCreate(request)
    return render(request, 'index.html')

def recommendationCreate(request):
    recommendation = Recommendation.objects.create(
            relationship=request.POST.get('relationship'),
            closeness=int(request.POST.get('closeness')),
            duration=int(request.POST.get('duration')),
            region=request.POST.get('region'),
            attendance=request.POST.get('attendance'),
            budget_min=request.POST.get('budget_min') or None,
            budget_max=request.POST.get('budget_max') or None,
            additional_info=request.POST.get('additionalInfo', '')
        )
    return render(request, 'result.html', {'recommendation': recommendation})