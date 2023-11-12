from django.shortcuts import render
def index(request):
    template = {
        "person_name" : "abboud",
        "company":"Matrix Master",
        "ship_date":"2020-1-1",
        "item_list":["first", "second", "third"],
        "ordered_warranty":True,
    }

    template_name = 'polls/index.html'
    return render(request, template_name, template)