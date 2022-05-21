from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

template = Jinja2Templates(directory='templates')

app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name='static')

@app.get("/")
def first_page(request: Request):
    names = ['Noufal', 'Gokul', 'Rahul']
    return template.TemplateResponse(
        'index.html',
        context={
            'request': request,
            'names': names,
            'title': 'Home Page'
        }
    )

@app.get("/about")
def about_us(req: Request):
    return template.TemplateResponse(
        'about.html',
        context={
            'request': req,
            'title': 'About US'
        }
    )