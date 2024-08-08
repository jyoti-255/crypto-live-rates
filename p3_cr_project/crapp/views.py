from django.shortcuts import render
from requests import get

def home(request):
    if request.GET.get("coin"):
        coin = request.GET.get("coin")
        try:
            a1 = "http://api.coinlayer.com/live"
            a2 = "?access_key=" + "a71df52581b33e8fc0b25a85f7ed6489"
            url = a1 + a2
            res = get(url)
            data = res.json()
            msg = data["rates"][coin]
            msg = "$" + str(round(msg, 2))
            return render(request, "home.html", {"msg": msg})
        except Exception as e:
            msg = "issue: " + str(e)
            return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")
