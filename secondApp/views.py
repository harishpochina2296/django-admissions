from django.shortcuts import render


# Create your views here.
def feeCollection(request):
        return render(request, 'secondApp/fee-collected.html')
 

def feeDuesReport(request):
    return render(request, 'secondApp/feedues-report.html')
 


def feeCollectionReport(request):
    return render(request, 'secondApp/feecollection-report.html')
