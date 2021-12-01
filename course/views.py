from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Course, Event, Location

from .forms import CourseForm, NotificationForm

from datetime import datetime

from .tools import generateCalendarEntries, getBuildingCode

# Create your views here.

@login_required(login_url='/login')
def myClasses(request):

    classes = Course.objects.filter(student = request.user.id)

    events = Event.objects.filter(student = request.user.id).order_by('date').filter(date__gte=datetime.today())[0:3]

    calendarEvents = generateCalendarEntries(request.user.id)

    context = {
        'classes' : classes,
        'notifications' : events,
        'calendarEvents' : calendarEvents
    }

    return render(request, 'myclasses.html', context)

@login_required(login_url='/login')
def getSchedule(request):
    return render(request, 'getschedule.html')

@login_required(login_url='/login')
def addClass(request):
    form = CourseForm()
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            newCourse = Course(
                student = request.user,
                course_code = form.data['course_code'],
                course_name = form.data['course_name'],
                section = form.data['section'],
                credits = form.data['credits'],
                schedule = form.data['schedule'],
                classroom = form.data['classroom'],
                professor = form.data['professor']
            )
            newCourse.save()

            return redirect('/myclasses')


    context = {'form' : form}
    return render(request, 'addclass.html', context)  

@login_required(login_url='/login')
def addNotification(request):
    form = NotificationForm()
    
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        print("Name = " + form.data['name'])
        print("Date = " + form.data['date'])
        print("Description = " + form.data['description'])
        if form.is_valid():
            newEvent = Event(
                student = request.user,
                name = form.data['name'],
                date = form.data['date'],
                description = form.data['description'],
            )
            newEvent.save()

            return redirect('/notifications')

        else:
            print("Form is invalid")
            print(form.errors)
        


    context = {'form' : form}
    return render(request, 'addnotification.html', context) 

@login_required(login_url='/login')
def class_info(request, class_code):
    
    try:
        selected_class = Course.objects.filter(student = request.user.id, course_code = class_code)
        context = {
            'class_found': True,
            'class_code': selected_class[0].course_code,
            'class_name': selected_class[0].course_name
        }

        buildingCode = getBuildingCode(selected_class[0].classroom)

        if(buildingCode != "unknown"):
            building = Location.objects.filter(building_code = buildingCode)
            
            context['map_frame'] = building[0].embed
            context['building_name'] = building[0].building_name

        return render(request, 'class_info.html', context)

    except Exception as exc:
        return render(request, 'class_info.html', {
            'class_found': False
        })

def location_list(request):
    
    locations = Location.objects.all()

    context = {
        'locations': locations
    }
    
    return render(request, 'locations.html', context)

def notifications(request):

    events = Event.objects.filter(student = request.user.id).order_by('date').filter(date__gte=datetime.today())

    calendarEvents = generateCalendarEntries(request.user.id)

    context = {
        'notifications' : events,
        'calendarEvents' : calendarEvents
    }

    return render(request, 'notifications.html', context)

def deleteEvent(request, event_id):

    event = Event.objects.filter(student = request.user.id).filter(id = event_id)

    event.delete()

    return redirect('/notifications')

def deleteClass(request, class_id):

    course = Course.objects.filter(student = request.user.id).filter(id = class_id)

    course.delete()

    return redirect('/myclasses')