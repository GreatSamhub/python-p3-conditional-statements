#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65 and temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature < 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"
    pass

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
