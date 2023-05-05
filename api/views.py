from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create a function based view to render student information to front end.
def student_details(request, pk):
    # Retrieve a single model object (row) from Student table through a specific id. 
    student = Student.objects.get(id=pk)
    # Convert model object (complex data) into Python data (serialized data).
    serializer = StudentSerializer(student)
    # Here serializer.data is a dict object.
    return JsonResponse(serializer.data)

# Create a function based view to render all model instances (querysets) to front end.
def student_list(request):
    # Retrieve queryset from the database. 
    students = Student.objects.all()
    # Convert model object (complex data) into Python data (serialized data).
    serializer = StudentSerializer(students, many=True)
    '''
    In the above views.py file the first method ‘student_details’ returns
    ‘serializer.data’ that is a dict object which is allowed to be passed
    to the method JsonResponse() and by default it’s second parameter 
    safe=True. We know that when safe=True, the method JsonResponse() 
    only allows the dict object. In the below line of code I mentioned 
    the default value of ‘safe’ parameter.
    return JsonResponse(serializer.data)
    To solve the error I have to set ‘safe=False’ in the following code.
    '''
    return JsonResponse(serializer.data, safe=False)

'''
# Create a function based view to render student information to front end.
def student_details(request, pk):
    # Retrieve a single model object (row) from the database through a specific id. 
    student = Student.objects.get(id=pk)
    # Convert model object (complex data) into Python data (serialized data).
    serializer = StudentSerializer(student)
    # Convert python data into json data.
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    # Return json data to front end.
    # content_type = 'application/json', indicates that json data is sent to front end.
    return HttpResponse(json_data, content_type = 'application/json')


# Create a function based view to render all model instances (queryset) to front end.
def student_list(request):
    # Retrieve all model objects (rows) from the database.
    students = Student.objects.all()
    # Convert model objects (complex data) into Python data (serialized data).
    serializer = StudentSerializer(students, many=True)
    # Convert python data into json data.
    json_data = JSONRenderer().render(serializer.data)
    # Show JSON data in terminal.
    print(json_data)
    # Return json data to front end.
    # content_type = 'application/json', indicates that json data is sent to front end.
    return HttpResponse(json_data, content_type = 'application/json')
    '''




