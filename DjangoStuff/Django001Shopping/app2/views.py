from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('''<html>
    <head>
        hey <HR color="red" height="2000">
    </head>
    <body>  
        <ol>
            <li> Fruits 
                <ol>
                    <li> Mango </li>
                    <li> Orange </li>
                </ol>
            </li>

            <li> Vegetables
                <ol>
                    <li> Cabbage </li>
                    <li> Capsicum 
                        <ol>
                            <li> green </li>
                            <li> yellow </li>
                            <li> red </li>
                        </ol>
                    </li>
                </ol>
            </li>

        </ol>
    </body>
</html>''')
