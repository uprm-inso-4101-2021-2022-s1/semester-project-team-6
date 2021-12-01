from django.forms import ModelForm
from .models import Course
from .models import Event

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['course_code', 'course_name', 'section', 'credits', 'schedule', 'classroom', 'professor']

class NotificationForm(ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'date', 'description']