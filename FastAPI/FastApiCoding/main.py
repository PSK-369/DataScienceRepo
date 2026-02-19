from fastapi import FastAPI, HTTPException, Request
from sqlalchemy import create_engine
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from types import validations

app = FastAPI(title="My first app", description="this is first api app", version="1.0")


# main routes


@app.get("/main")
def welcome_page():
    return {"message": "helloworld"}


@app.get("/login")
def login_page():
    return "this is my login page"


@app.get("/logout")
def logout_page():
    return "this is my logout page"


@app.get("/filterpage")
def filter_page():
    return "this is my filter page"


@app.get("/{id}")
def dynamic_data(id: int) -> str:
    return f"this dynamice page {id}"


@app.post("/todo")
def create_todo(item: dict):
    return f"{item}"


@app.get("/one")
def root(request: Request):
    params = request.query_params
    return {"params": params}
