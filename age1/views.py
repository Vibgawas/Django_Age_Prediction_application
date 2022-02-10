from msilib.schema import Error
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def index(request):
    
    return render(request,'base.html')



def get_age1(dob):
    todays_date = date.today()
    age_year = todays_date.year - dob.year

    if (todays_date.month, todays_date.day)>(dob.month,dob.day):
        x = 0
    else:
        x = 1

    age_year = age_year-x
    
    return age_year
    

def getage(request):
    a = request.GET.get('dobirth')
    Error_message = None
    age = None
    try:
        d,m,y = a.split('-')
        b= date(int(y),int(m),int(d))
        age = get_age1(b)
    except:
        Error_message = "Something went wrong !!! Please check your input........."
    
    
    data = {'error':Error_message,
            'value':age,
            'user_dob':a}
    

    return render(request,'base.html',data)