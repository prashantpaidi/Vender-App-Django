from django.shortcuts import redirect, render
from .models import Bid, Tender,Tenderwinner
from django.db import connection
import datetime



def dashborad(request):
    if request.user.is_authenticated:
        tender = Tender.objects.order_by('-start_date')
        tenderdata = tender[:5]
        user = request.user
        tenderwon = Tenderwinner.objects.select_related('tender').filter(user=user).order_by('-id')
        tenderwondata = tenderwon[:5]
        onofbiduser = Bid.objects.all().filter(user=user).count()
        onofactive=Tender.objects.filter(end_date__gt=datetime.date.today()).count()
        onoftenderwon =tenderwon.count()
        onoftender =tender.count()
        return render(request, "dashboard.html", {'tenderdata': tenderdata,'tenderwondata':tenderwondata,'onofbiduser':onofbiduser,'onofactive':onofactive,'onoftenderwon':onoftenderwon,'onoftender':onoftender})
    else:
        return redirect('login')

def all(request):

    tenderdata = Tender.objects.all()

    if request.user.is_authenticated:
        return render(request, "all.html", {'tenderdata': tenderdata})
    else:
        return redirect('login')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]




def bidedit(request, pk_bid):
    editflag = False
    if request.user.is_authenticated:
        if Tender.objects.filter(id=pk_bid,end_date__gt=datetime.date.today()).exists():
            tender=Tender.objects.get(id=pk_bid)
            user = request.user
            bid = Bid.objects.filter(tender=tender).filter(user=user)
            if request.method == 'POST':
                bidvalue = request.POST['bidvalue']
                if bid.exists():
                    bid = Bid(bid[0].id,bid_price=bidvalue,user=user, tender=tender)
                    bid.save()
                    return redirect("bidview", pk_bid)
                else:
                    bid = Bid(bid_price=bidvalue,user=user, tender=pk_bid)
                    bid.save()
                    return redirect("bidview", pk_bid)
            if bid.exists():
                return render(request, "singlebid.html", {'tender': tender, 'bidvalue':bid[0].bid_price})

            else:
                return render(request, "singlebid.html", {'tender': tender})
           
        else:
            return redirect("bidview", pk_bid)


    else:
        return redirect('login')

def bidview(request, pk_bid):
    # check expere of exists 
    tender=Tender.objects.get(id=pk_bid)
    if request.user.is_authenticated:
        user = request.user
        bid = Bid.objects.filter(tender=tender, user=user)
        tendercond = Tender.objects.filter(id=pk_bid,end_date__lt=datetime.date.today())
        errormsg='Last of submission is over'
        if(bid.exists() and tendercond.exists()):
            bidprice= bid[0].bid_price
            return render(request, "viewsinglebid.html", {'tender': tender,'bidprice':bidprice,'errormsg':errormsg})
        elif tendercond.exists():
            return render(request, "viewsinglebid.html", {'tender': tender,'errormsg':errormsg})
        elif bid.exists():
            bidprice= bid[0].bid_price
            return render(request, "viewsinglebid.html", {'tender': tender,'bidprice':bidprice})
        return render(request, "viewsinglebid.html", {'tender': tender})
    else:
        return redirect('login')


def active(request):

    tenderdata=Tender.objects.filter(end_date__gt=datetime.date.today())
    if request.user.is_authenticated:
        return render(request, "active.html", {'tenderdata': tenderdata})
    else:
        return redirect('login')


def inactive(request):
    tenderdata=Tender.objects.filter(end_date__lt=datetime.date.today())

    if request.user.is_authenticated:
        return render(request, "inactive.html", {'tenderdata': tenderdata})
    else:
        return redirect('login')


def applied(request):
    if request.user.is_authenticated:
        user = request.user
        tenderdata = Bid.objects.all().select_related('tender').filter(user=user)
        for tender in tenderdata:
            print(tender.tender.tender_name)
        return render(request, "applied.html", {'tenderdata': tenderdata})
    else:
        return redirect('login')


def unapplied(request):
    cursor = connection.cursor()
    cursor.execute("SELECT public.tender_tender.id, public.tender_tender.tender_name, public.tender_tender.tender_description, public.tender_tender.start_date, public.tender_tender.end_date FROM (SELECT * FROM tender_bid WHERE tender_bid.user_id = 2) AS derivedTable FULL OUTER JOIN tender_tender ON derivedTable.tender_id = tender_tender.id WHERE derivedTable.user_id is NOT NULL")
    tenderdata = dictfetchall(cursor)
    for tender in tenderdata:
        print(tender["tender_name"])
    if request.user.is_authenticated:
        return render(request, "unapplied.html", {'tenderdata': tenderdata})
    else:
        return redirect('login')






def won(request):

    if request.user.is_authenticated:
        user = request.user
        tenderwondata = Tenderwinner.objects.select_related('tender').filter(user=user)
        return render(request, "won.html", {'tenderwondata': tenderwondata})
    else:
        return redirect('login')