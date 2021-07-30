from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render

from . import models
from .forms.RegisterBookForm import RegisterBook
from .forms.DeleteBookForm import DeleteBook


# Create your views here.
def HomePage(request):
    try:
        search_string = request.GET.get('search_str', None)
        searh_by = request.GET.get('search_by', None)

        book_list = models.getBooks(search_string, searh_by)
        print(searh_by, search_string)
        return render(request, 'HomePage.html', {
            "book_list": book_list
        })
    except IndexError as e:
        print(str(e))
        return render(request, 'HomePage.html', {
            "book_list": []
        })

    except Exception as e:
        print(str(e))
        return render(request, 'HomePage.html', {
            "book_list": []
        })


def addBookPage(request):
    return render(request,
                  'addBook.html'
                  )


def deleteBookPage(request):
    return render(request,
                  'deleteBook.html'
                  )


def deleteBook(request):
    try:
        if request.method == 'POST':
            form = DeleteBook(request.POST)

            if form.is_valid():
                models.deleteBook(request.POST['title'])
                return HttpResponseRedirect('/?success=Successfully book deleted')

            else:
                raise Exception("data is invalid")
        else:
            form = DeleteBook()

        return render(request, 'deleteBook.html', {'form': form})

    except Exception as e:
        print(str(e))
        return HttpResponseRedirect(f'/delete?error="error while deleting a book:{str(e)}')


def addBook(request):
    try:

        if request.method == 'POST':
            form = RegisterBook(request.POST)

            if form.is_valid():
                models.addBook(request.POST['title'],
                               request.POST['author'],
                               request.POST['genre'],
                               request.POST['height'],
                               request.POST['publisher'])

                return HttpResponseRedirect('/?success=Successfully data added')
            else:
                raise Exception("data is invalid")

        else:
            form = RegisterBook()

        return render(request, 'addBook.html', {'form': form})

    except Exception as e:
        print(str(e))
        return redirect(f'/add?error="error while adding a book:{str(e)}')
