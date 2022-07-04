from datetime import datetime
from django.shortcuts import  render, redirect
from .forms import NewUserForm #,requestbook_form #,issuebook_form
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from .models import Book,request_book

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			if request.POST['usertype']=='librarian':
				user.is_staff = True
				user.save()
			else:
				user.is_staff=False
				user.save()
			login(request, user)
			return redirect("signup")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"register.html",{"form":form})

def signup(request):
	if request.method == "POST":
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				if user.is_staff==True:
					return redirect('librarian')
				else:
					return redirect('student')
				
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"login.html", {"login_form":form})
def logoutview(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect(register)

def librarian(request):
	book=Book.objects.all()
	return render(request,'librarian.html',{'book':book})

def add(request):
	if request.method=="GET":
		return render(request,'addbook.html')
	else:
		Book(
			book_name=request.POST.get('bname'),
			author=request.POST.get('aname'),
   			published_date= request.POST.get('date')
		).save()
		return redirect('librarian')
def update(request,id):
	if request.method=="GET":
		updatebook=Book.objects.get(id=id)
		return render(request,'update.html',{'updatebook':updatebook})
	else:
		updatebook=Book.objects.get(id=id)
		updatebook.book_name=request.POST['bname']
		updatebook.author=request.POST['aname']
		updatebook.published_date= request.POST['date']
		updatebook.save()
		return redirect('librarian')

def deletebook(request,id):
	delbook=Book.objects.get(id=id)
	delbook.delete()
	return redirect('librarian')

def requestbook(request):
	if request.user.is_staff == False:
		booksLst = Book.objects.filter(book_count__gt = 0)
		print("bookslst", booksLst)
		if request.method == "POST" :
			update_book_count = Book.objects.get(id = request.POST['req_book'])
			request_book.objects.create(book_name = update_book_count, student_name = request.user, request_date = datetime.now(), status = "Pending")
			print(request.POST['req_book'])
			# update_book_count.book_count = (update_book_count.book_count)-1
		return render(request,'student.html',{'booksLst':booksLst})
			 
	else:
		return HttpResponse('Has no access to request book')
def booklist(request):
	book=Book.objects.all()
	return render(request,'booklist.html',{'book':book})


# def issuebook(request):
# 	if request.method=="POST":
# 		form=issuebook_form(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			form=issuebook_form()
# 			return render(request,'issuebook.html',{'form':form})
		
# 		else:
# 			return HttpResponse('invalid form')
		
# 	else:
# 		form=issuebook_form()
# 		return render(request,'issuebook.html',{'form':form})

#def studentview(request):
	# if request.method=="POST":
	# 	form=requestbook_form(request.POST)
	# 	if form.is_valid():
	# 		print("form", form)
	# 		form.save()
	# 		form=requestbook_form()
	# 		return render(request,'student.html',{'form':form})
		
	# 	else:
	# 		return HttpResponse('invalid form')
		
	# else:
	# 	form=requestbook_form()
	# 	return render(request,'student.html',{'form':form})

def issuebook(request):
	pending_book=request_book.objects.filter(status="Pending")
	return render(request,'pending.html',{'pending_book':pending_book})

def approvebook(request,id):
	approve_book=request_book.objects.get(id=id)
	approve_book.status="Approved" 
	approve_book.save()
	book=Book.objects.get(book_name=approve_book.book_name)
	book.book_count=book.book_count-1
	book.save()
	return render(request,'approve.html',{'approve_book':approve_book})
def decline(request,id):
	decline_req=request_book.objects.get(id=id)
	decline_req.status="Cancelled"
	decline_req.save()
	return redirect('/issuebook')

