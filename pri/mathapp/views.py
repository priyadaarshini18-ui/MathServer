from django.shortcuts import render
def rate(request):
    km = int(request.POST.get('distance', 0))
    l= int(request.POST.get('fuel',0))
    rate = km/l if request.method == 'POST' else 0
    print("Distance=",km)
    print("Time=",l)
    print("rate=",rate)
    return render(request, 'mathapp/pri.html', {'km': km, 'l': l, 'rate': rate})



