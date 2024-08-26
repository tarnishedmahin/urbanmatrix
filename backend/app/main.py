from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import api_router
from app.db.databse import get_db
from app.utils.security import get_current_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#for testing
@app.get("/user")
def read_items(db = Depends(get_db), current_user: dict = Depends(get_current_user) ):
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        items = cursor.fetchall()
    print(current_user)
    return items

app.include_router(api_router, prefix="/api")
