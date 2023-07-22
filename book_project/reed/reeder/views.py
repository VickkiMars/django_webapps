from django.shortcuts import render, redirect
from .models import Book, Author, comment, Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import PyPDF2
# Create your views here.

Books = Book.objects.all()
Authors = Author.objects.all()
Popular = Book.objects.filter()
New = Book.objects.filter()
Fan_favourite = Book.objects.filter()
Top_authors = Author.objects.filter()

def get_page_number(book_path):
    file = open(book_path, 'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    totalpages = readpdf.numPages
    return totalpages

def home(request):    
    context = {'books': Books, 'author':Authors}
    return render(request, "reeder/index.html", context)

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Login Credentials")
            return redirect('signin')
    else:
        return render(request, "reeder/signin.html")


def logout(request):
    auth.logout(request)
    return redirect('signin')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        gender = request.POST['mgender']
        password = request.POST['password']
        password2 = request.POST['confirm']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already in use")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signin')

        else:
            messages.info(request, "Passwords do not match")
            return redirect('signup')

    else:
        return render(request, 'reeder/signup.html')

# @login_required(login_url='signin')
def upload(request):
    if request.method == "POST":
        user = request.user.username
        book_file = request.FILES.get('book_upload')
        thumbnail_image = request.FILES.get('thumbnail_upload')
        author =  request.POST['author']
        title = request.POST['title']
        pub_date = request.POST['pub_date']
        description = request.POST['description']
        publishing_house = request.POST['press']
        lang = request.POST['language']
        category = request.POST['category']


        print(author)
        print(title)
        print(pub_date)
        print(description)
        print(book_file)


        
        author_object = Author(name=author)
        author_object.save()
        up_auth = Author.objects.filter(name=author)
        upauth = up_auth[0]
        new_book = Book.objects.create(uploaded_by=user, book=book_file, thumbnail=thumbnail_image, description=description, pub_date=pub_date, title=title, author=upauth, language = lang, category = category, press=publishing_house)
        new_book.save()

        return redirect('/')
    else:
        return redirect('/')


def uploading(request):
    return render(request, 'reeder/uploading.html')

def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.profileimg

            user_profile.profileimg = image
            user_profile.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            user_profile.profileimg = image
            user_profile.save()

        return redirect('profile')

    return render(request, 'reeder/profile.html', {'user_profile': user_profile})
