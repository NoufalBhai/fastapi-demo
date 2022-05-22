# <center>BrickAr Backend API</center>

## Table of Content
 - [Technologies Used](#tech-used)
 - [Framework and Packages](#framework-and-packages)
    + [Python Poetry](#python-poetry)
    + [Packages](#packages)
        * [Application Dependencies](#application-dependencies)
        * [Dev Dependencies](#dev-dependencies)
 - [Developer Guide](#devloper-guidelines-memo)
    + [Precommit Hook (Mandatory)](#precommit-hook)
        * [What is pre-commit hook?](#what-is-pre-commit-hook)
        * [Implement pre-commit hook](#implement-pre-commit-hook)
 - [Run Application](#run-application)


 <h2 id="tech-used">Technologies Used</h2>
 
- Python :snake:
    - Using Python Version 3.9 or later
    - You can download and install python from <a href="https://www.python.org/" target="_blank">here</a>

- Postgres
    - Using Postgres SQL DataBase for Save Most of our data in structured manner
    - Using Version Postresql 12
    - You can down load and learn more about postgres <a href="https://www.postgresql.org/" target="_blank">here</a>
    - also a very good documentation is in <a href="https://www.postgresqltutorial.com/" target="_blank">postgresqltutorial</a>

- Severs :computer:
    - Initially Planned to deploy on AWS EC2 Instance

- Messaging Service
    - comming soon


## Framework and Packages

> For Package :package: Management We are using <a href="https://python-poetry.org/" target="_blank">python-poetry</a> instead of pip 

### Python Poetry
    
- Poetry is a python packaging and Dependency Management System
- Simple and Easy to Use
- Go through the <a href="https://python-poetry.org/docs/" target="_blank">Documentation</a> to get a quick gasp

> This Docs will Explain All the poetry commands you need for this development in Application Development Section

### Packages

#### Application Dependencies

1. **<ins>FastAPI</ins>:** 

    FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. 

    Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available. <a href="https://fastapi.tiangolo.com/" target="_blank">Learn More about FastAPI</a>
    > we are using `FastAPI 0.75.0`

2. **<u>Alembic:</u>** 

    Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python. Checkout the <a href="https://alembic.sqlalchemy.org/en/latest/" target="_blank">documentation</a> of alembic for more details
    > we are using `alembic 1.7.6` 

3. **<u>SQLAlchemy</u>**: 
    
    SQLAlchemy the Python SQL toolkit and <acronym title="Object Relational Mapper">ORM</acronym> that gives application developers the full power and flexibility of SQL. Know more about <a href="https://docs.sqlalchemy.org/en/14/" target="_blank">SQLAlchemy</a>.
    > we are using `SQLAlchemy 1.4.32`

4. **<u>pscopg2</u>:** 

    psycopg2 is the most popular PostgreSQL database adapter for the Python programming language. Used for connecting Postgres DataBase to our application Using SQLAlchemy <acronym title="Object Relational Mapper">ORM</acronym>. <a href="https://www.psycopg.org/docs/" target="_blank">Official Documentation</a>.
    > we are using `psycopg2 2.9.3`
 
5. **<u>Uvicorn :unicorn: :</u>** 
    
    Uvicorn is an <acronym title="Asynchronous Server Gateway Interface">ASGI</acronym> web server implementation for Python. <a href="https://www.uvicorn.org/" target="_blank">Read More</a>.

#### Dev Dependencies
For Development Purpose only we are using these packages, for Formatting,<a href="https://en.wikipedia.org/wiki/Lint_(software)" target="_blank">Linting</a>, and uinttest.

>We are enforcing <a href="https://www.python.org/dev/peps/pep-0008/" target="_blank">PEP8</a> Style Guide
1. flake8

    flake8 is a wrapper around some of the python linting packages, it will check code and find out the problems with in the .py files, <a href="https://flake8.pycqa.org/en/latest/" target="_blank">read more</a>.
2. black

    black is a code style guide enforce tool so who ever write the code it will automatically format on same way, <a href="https://black.readthedocs.io/en/stable/" target="_blank">black docs</a>
3. isort

    isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type. <a href="https://pypi.org/project/isort/" target="_blank"> documentation</a>.
4. pytest

    pytest is the unitttest library, it will help us to write unittest for each and every fuctionalities we are developing.
    Learn more about <a href="https://docs.pytest.org/en/stable/" target="_blank">pytest</a>.
5. pre-commit

    This package is used for enforcing all the linting and formatting of code.
    it will create a check before commit and check your commiting code changes, if it is properly formatted it will commit, otherwise it shows error. <a href="https://pre-commit.com/" target="_blank">docs</a>. More Implemetation details for our project is [below](#implement-precommit-hook)

## Devloper Guidelines :memo:

All The Developers on this project must enforce these Guide lines.
We are Enforcing All Users to Use <a href="https://www.python.org/dev/peps/pep-0008/" target="_blank">PEP8</a>. For that we are using <a href="https://black.readthedocs.io/en/stable/" target="_blank">black</a> and <a href="https://pycqa.github.io/isort/" target="_blank">isort</a>. To follow these rules we are enforcing this via pre-commit-hooks

### Precommit Hook

> By setting up the pre-commit hook this will enforce you all the style guides and coding standards

#### What is pre-commit hook?

pre-commit hooks are a mechanism of the version control system git. They let you execute code right before the commit. Confusingly, there is also a Python package called pre-commit which allows you to create and use pre-commit hooks with a way simpler interface. The Python package has a plugin-system to create git pre-commit hooks automatically. It’s not only for Python projects but for any project.

#### Implement pre-commit hook

When you clone this repo there is a file called `.pre-commit-config.yaml` don't cahnge anything :no_entry: on this file. Mostly this will be managed by the Team/Repo Admin :cowboy_hat_face: .

+ Create a Virtual Environment for your project

    there is several methods for create the virtual environment

    * using python's `venv` module command `python -m venv name-of-venv` 
    * using virtualenv module. see the <a href="https://virtualenv.pypa.io/en/latest/user_guide.html" target="_blank">docs</a>.
    * using poetry shell command <a href="https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment" target="_blank">See the Docs</a>.

+ To implement hook in your local clone you  need to install all requirements by running poetry command `poetry install --no-root`
It will Install all requirements including Dev Dependencies

+ After that you can run `pre-commit install` command

+ After that you are good to go :satisfied:

><strong style="color:red;">Note:</strong> <i>Eventhough you can bypass pre-commit hook using `git commit --no-verify` command, don't use this command on your development cycle, all the codes are reviewed in the time of merge by github actions (automation :robot:) and by persons (repo  admin :cowboy_hat_face: ).</i>

## Run Application

