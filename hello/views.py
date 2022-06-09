from django.shortcuts import render
from .models import Friend
from .forms import FindForm,CheckForm,FriendForm
from django.db.models import Count,Sum,Avg,Min,Max
from django.core.paginator import Paginator
# Create your views here.
def index(request , num=1 ):
    data = Friend.objects.all().order_by('age').reverse()
    re1 = Friend.objects.aggregate(Count('age'))
    re2 = Friend.objects.aggregate(Avg('age'))
    re3 = Friend.objects.aggregate(Sum('age'))
    page = Paginator( data , 3 )
    params = {
        'msg' : "{} {} {}".format(re1,re2,re3),
        'data':page.get_page( num )
    }
    return render( request, "hello/index.html" , params )

def find( request ):
    if(request.method=="POST"):
        msg = request.POST['find']
        name = request.POST['findName']
        mail = request.POST['findMail']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if( msg != '' ):
            sql += ' where ' + msg
        if( name != '' ):
            sql += " where name='{}'".format(name)
        if( mail != '' ):
            sql += " where mail like '%{}%'".format(mail)
        if( 'order' in request.POST ):
            sql += " order by age desc"
        else:
            sql += " order by age asc"
        print( sql )
        data = Friend.objects.raw( sql )
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data
    }
    return render( request,'hello/find.html',params )

def check( request ):
    params = {
        'title' : 'Hello',
        'message' : 'check validation.',
        'form':FriendForm()
    }
    if(request.method=='POST'):
        form = FriendForm(request.POST)
        params['form'] = form
        if( form.is_valid()):
            params['message'] = 'OK'
        else:
            params['message'] = 'no good'
        
    return render( request , 'hello/check.html' , params )