from fastapi import FastAPI, HTTPException, Body
from firebase_admin import credentials, firestore, initialize_app
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

