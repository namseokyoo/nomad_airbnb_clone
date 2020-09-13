from math import ceil
from datetime import datetime
from django.urls import reverse
from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """ Home view Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    ordering = "created"
    # page_kwarg = "potato"
    context_object_name = "rooms"

    def get_context_data(self, **kwags):
        context = super().get_context_data(**kwags)
        now = timezone.now()
        context["now"] = now
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
        # return redirect(reverse("core:home"))


# paginator FBV
# def all_rooms(request):
#     page = request.GET.get("page")
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.get_page(page)
#         return render(
#             request,
#             "rooms/home.html",
#             context={
#                 "page": rooms,
#             },
#         )
#     except EmptyPage:
#         return redirect("/")


# pagination manualy
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     page = int(page or 1)
#     page_size = 10
#     limit = page_size * page
#     offset = limit - page_size
#     all_rooms = models.Room.objects.all()[offset:limit]
#     page_count = ceil(models.Room.objects.count() / page_size)
#     return render(
#         request,
#         "rooms/home.html",
#         context={
#             "rooms": all_rooms,
#             "page": page,
#             "page_count": page_count,
#             "page_range": range(1, page_count + 1),
#         },
#     )