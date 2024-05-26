from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from datetime import datetime, time


# Create your views here.
def home(request):
    if request.method == "POST":
        bookingForm = BookRoomForm(request.POST)
        if bookingForm.is_valid():
            bookingForm.save()
            messages.success(request, "Room Booked!")
            return redirect("home")
    else:
        bookingForm = BookRoomForm()

    return render(
        request,
        "home.html",
        {
            "bookingForm": bookingForm,
        },
    )


def dashboard(request):
    # book_id = get_object_or_404(BookRoom, id=id)
    # print(book_id)
    bookedRooms = BookRoom.objects.all()
    return render(request, "dashboard.html", {"bookedRooms": bookedRooms})


def viewBook(request, id=None):
    books = {}
    book = get_object_or_404(BookRoom, id=id)
    bookform = BookRoomForm(request.POST, instance=book)
    if bookform.is_valid():
        bookform.save()
        messages.success(request, "Booking Updated!")
        return redirect("dashboard", id=book)
    bookform = BookRoomForm(instance=book)
    books["bookform"] = bookform

    bookedRooms = BookRoom.objects.all()
    #### CALENDAR #####
    bookings = []
    customer_book = BookRoom.objects.filter(id=book.id)
    for book in customer_book:
        start_datetime = datetime.combine(book.arrive_date, book.time)
        end_datetime = datetime.combine(
            book.departure_date, datetime.strptime("10:00:00", "%H:%M:%S").time()
        )

        booking = {
            "title": book.full_name,
            "start": start_datetime.isoformat(),
            "end": end_datetime.isoformat(),
        }
        bookings.append(booking)

    return render(
        request,
        "dashboard.html",
        {
            "bookedRooms": bookedRooms,
            "bookform": bookform,
            "bookings": bookings,
        },
    )
