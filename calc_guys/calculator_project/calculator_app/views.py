from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
    result = None

    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Division by zero is not allowed."

    elif request.method == 'GET':
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')
        operation = request.GET.get('operation')

        if num1 is not None and num2 is not None and operation is not None:
            num1 = float(num1)
            num2 = float(num2)

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Division by zero is not allowed."

    return render(request, 'calculator.html', {'result': result})

