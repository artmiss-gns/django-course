from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
# Create your views here.

challenges = {
    'January': '10 push-ups',
    'February': '20 sit-ups',
    'March': '30 jumping jacks',
    'April': '10 minute walk',
    'May': '20 tricep dips',
    'June': '30 seconds of plank',
    'July': '10 burpees',
    'August': '20 bicep curls',
    'September': '30 seconds of wall sit',
    'October': '10 mountain climbers',
    'November': '20 leg raises',
    'December': '30 seconds of jogging in place'
}

def index(request):
    return render(request, 'challenges/index.html')

def monthly_challenges(request, month):
    month = month.title() # to match it to our data
    try: 
        task = challenges[month]
        # return HttpResponse(f"{month}: {task}")
        return render(
            request,
            'challenges/challenges.html',
            context={
                'month': month,
                'task': task,
            }
        )
        
    except KeyError:
        raise Http404(f"{month} is not a valid month!")
    
def numeric_monthly_challenges(request, month):
    if month > 12 or month < 1 :
        raise Http404(f"{month} is not a valid numeric month!")
    
    month = list(challenges.keys())[month-1]
    redirected_path = reverse('month_challenges', args=[month])
    return HttpResponseRedirect(
        redirect_to=redirected_path
    )
    