import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })

# now = datetime.datetime.now()
# print(f"this is now {now}")
# print(f"this is month {now.month}")
# print(f"this is day {now.day}")
# print(f"this is year {now.year}")