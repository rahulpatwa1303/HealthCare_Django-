from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == "POST":
       msg_name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       subject = request.POST['subject']
       message = request.POST['message']

       send_mail(
            subject,
            message,
            email,
            phone,
            ['rahul.y2j@gmail.com'],
       )        

       return render(request, 'contact.html', {'msg_name' : msg_name})
    else:
        return render(request, 'contact.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def appointment(request):

    if request.method == "POST":
       msg_name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']
       Department = request.POST['Department']
       Doctor = request.POST['Doctor']
       date = request.POST['date']
      
      
       appointment = 'Name by whom appointment has been placed' + msg_name + " email address of the appointment holder " + email + " phone number of the appointment holder: " + phone + " Date for the appointment: " +  date + " Requested doctor and the deparment: " + Doctor + " " + Department

       send_mail(
            'Appointment request, please find details below',    #subject,
            appointment,
            email,
            phone,
            ['rahul.y2j@gmail.com'],
       )        
      
       return render(request, 'appointment.html', {
           'msg_name' : msg_name,
           'email' : email,
           'Department' : Department,
           'Doctor' : Doctor,
           'date' : date,
           'phone' : phone,
           'message' : message,
           })
    else:
        return render(request, 'index.html', {}) 

    