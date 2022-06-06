from django.shortcuts import render
from .models import Friend
from .forms import FindForm
from django.db.models import Count,Sum,Avg,Min,Max

# Create your views here.
def index(request):
    data = Friend.objects.all().order_by('age').reverse()
    re1 = Friend.objects.aggregate(Count('age'))
    re2 = Friend.objects.aggregate(Avg('age'))
    re3 = Friend.objects.aggregate(Sum('age'))
    params = {
        'msg' : "{} {} {}".format(re1,re2,re3),
        'data':data
    }
    return render( request, "hello/index.html" , params )

def find( request ):
    