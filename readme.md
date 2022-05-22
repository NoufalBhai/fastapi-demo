Web -> HTML + CSS + JavaScript

FastAPI
---
Route = Urls
/ - Index Page/First Page

Jija2 Templating Engine is used for render HTML
Jinja2 is used for passing and adding data to HTML via python

1. Install Jinja2
2. from fastapi.templating import Jinja2Templates
3. template = Jinja2Templates(directory='templates')
    'templates' is the folder name in which all the html files resides
4. Setting UP Static Files
    - from fastapi.staticfiles import StaticFiles
    - adding a url called /static for access static files
        app.mount("/static", StaticFiles(directory='static'), name='static')
        *directory='static'* is the folder in which all static content like css, js, images 
5. Rendering a route (/)
    - Create an HTML File inside of template directory eg: index.html
    - from fastapi import Reruest
    - Create a python function with parameter request: Request <br>
        ` def first_page(request: Request): `
    - return object of TemplateResponse with html file and a context
        ``` 
        return template.TemplateResponse(
            'about.html',
            context={
                'request': req,
                'title': 'About US'
            }
        ) 
        ```

    