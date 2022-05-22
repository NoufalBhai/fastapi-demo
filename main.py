from fastapi import FastAPI, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from psycopg2 import connect

template = Jinja2Templates(directory='templates')

app = FastAPI()

conn = connect(
    host='localhost',
    port=5432,
    database="demo-app",
    user="postgres",
    password="password"
)

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


@app.get("/person")
def person_page(request: Request):
    return template.TemplateResponse(
        'person.html',
        context={
            'request': request
        }
    )

@app.post("/person")
def person_create(request: Request, name:str = Form(), age:int = Form(), email:str = Form()):
    conn.reset()
    cursor = conn.cursor()
    query = """
    INSERT INTO "fastapi-demo".person(name, age, email)
    VALUES (%s, %s, %s) RETURNING id
    """
    cursor.execute(query, (name, age, email))
    conn.commit()
    id = cursor.fetchone()[0]
    return RedirectResponse(url="/person", status_code=status.HTTP_302_FOUND)
    # return template.TemplateResponse(
    #     'person-saved.html',
    #     context= {
    #         'request': request,
    #         'name': name,
    #         'age': age,
    #         'email': email,
    #         "id": id
    #     }
    # )

@app.get("/{data}")
def index_data(data: int):
    return f"{data} {type(data)}"