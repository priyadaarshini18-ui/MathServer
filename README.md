# Ex.04 Design a Website for Server Side Processing
## Date:11/12/2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
pri.html

<html>
<head>
    <title>rate</title>
    <style>
        body {
           font:century ;
           background-color: rgb(255, 0, 128);
           font-size: 20px
}
        
        .box {
            width: 700px;
            margin: auto;
            margin-top: 120px;
            padding: 50px;
            background-color: #a2ffec;
            color: rgb(31, 26, 27);
            border: 4px dashed rgb(118, 72, 109);
            text-align: center;
            font-size: 18px
            
            
        }
        input {
            padding: 5px;
            margin: 8px;
            font-size: 20px
        }
        .btn {
            padding: 8px 15px;
            cursor: pointer;
            font-size: 15px
        }
    </style>
</head>

<body
    <div class="edge">
    <div class="box">
        <h1>consumption rate Calculator</h1>
        <h2> PRIYADAARSHINI V (25013541)<h2>
        

        <form method="POST">
            {% csrf_token %}
            Distance :<input type="text" name="distance" value="{{ km }}"><br>
            Fuel: <input type="text" name="fuel" value="{{ l }}"><br>

            <button class="btn" type="submit">Calculate</button><br><br>

            rate:
            <input type="text" value="{{ rate }}" readonly> km/l
    
        </form>
        </div>
    </div>

</body>
</html>
```
```
views.py

from django.shortcuts import render
def rate(request):
    km = int(request.POST.get('distance', 0))
    l= int(request.POST.get('fuel',0))
    rate = km/l if request.method == 'POST' else 0
    print("Distance=",km)
    print("Time=",l)
    print("rate=",rate)
    return render(request, 'mathapp/pri.html', {'km': km, 'l': l, 'rate': rate})
```
```
urls.py
 
 from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.rate, name='rate'),
]
```
## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2025-12-11 222256.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2025-12-11 222217.png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
