from fastapi import FastAPI
import database


app = FastAPI(title="Notes API")

def get_db():
    return database