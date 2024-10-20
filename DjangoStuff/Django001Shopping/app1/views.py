from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('''<html>
    <head>
        <style>
            #london{
                background-color: red;
                overflow: auto;
                padding: 100px;              
            }
            #oslo{
                background-color: blue;
                overflow: auto;
                float:inline-end;
                padding:100px;
                color:white;
            }
            #Rome{
                background-color: green;
                overflow:auto;
                padding:100px;
                
            }

            #delhi{
                background-color: yellow;
                overflow:visible;
                float:inline-end;
                padding:100px;
            }
        </style>
    </head>
    <body>
        <div id="london">
            <h2>London</h2>
            <p>London is the capital city of England.</p>
            <p>London has over 13 million inhabitants.</p>
          </div>
          
          <div id="oslo">
            <h2>Oslo</h2>
            <p>Oslo is the capital city of Norway.</p>
            <p>Oslo has over 600.000 inhabitants.</p>
          </div>
          
          <div id="delhi">
            <h2>Delhi</h2>
            <p>Delhi is the capital city of India.</p>
            <p>India is big dude.</p>
          </div>

          <div id="Rome">
            <h2>Rome</h2>
            <p>Rome is the capital city of Italy.</p>
            <p>Rome has almost 3 million inhabitants.</p>
            <video width="320" height="240" controls autoplay loop>
                <source src="sample.mp4" type="video/mp4" muted>
              Your browser does not support the video tag.
              </video>
          </div>
    </body>
</html>''')