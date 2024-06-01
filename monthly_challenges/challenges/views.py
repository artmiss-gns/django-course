from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
def main(request):
    return HttpResponse("HELLO WORLD")

def month_challenge(request, month:str):
    try :
        return HttpResponse(challenges[month.title()])
    except KeyError:
        return HttpResponseNotFound(f"Month not found: {month.title()}")
    
def numeric_month_challenge(request, month:int):
    try :
        month = list(challenges.keys())[month-1]
    except IndexError:
        return HttpResponseNotFound(f"Not valid input: {month}")
    # try :
    #     return HttpResponse(challenges[month.title()])
    # except KeyError:
    #     return HttpResponseNotFound(f"Month not found: {month.title()}")
    
    # instead of rewriting the code, we can redirect this address
    return HttpResponseRedirect(f'/challenges/{month}')