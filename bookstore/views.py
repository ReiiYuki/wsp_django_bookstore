from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book
from django.urls import reverse

def index(request) :
    book_list = Book.objects.all()
    try :
        book = Book.objects.get(book_id=int(request.session['session']))
    except KeyError :
        book = None
    return render(request,'index.html',{'book_list':book_list,'bookt':book})
def insert_book(request) :
    book = Book.objects.create(book_id = request.POST['book_id'],isbn = request.POST['isbn'],book_name = request.POST['book_name'],price = request.POST['price'],author = request.POST['author'])
    book.save()
    return HttpResponseRedirect(reverse('book:index'))
def delete_book(request):
    book = Book.objects.get(book_id=int(request.POST['book']))
    Book.delete(book)
    return HttpResponseRedirect(reverse('book:index'))
def update_request(request):
    request.session['session'] = request.POST['book_id']
    return HttpResponseRedirect(reverse('book:index'))
def update_book(request):
    book = Book.objects.get(book_id=request.POST['book_id'])
    book.book_id = request.POST['book_id']
    book.isbn = request.POST['isbn']
    book.price = request.POST['price']
    book.book_name = request.POST['book_name']
    book.author = request.POST['author']
    book.save()
    del request.session['session']
    return HttpResponseRedirect(reverse('book:index'))
