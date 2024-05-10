import bcrypt
from typing import Union
from fastapi import FastAPI, HTTPException
from app.models import User, UserLogging
from db.supabase import create_supabase_client
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize supabase client
supabase = create_supabase_client()

def user_exists(key: str = "email", value: str = None):
    user = supabase.from_("users").select("*").eq(key, value).execute()
    return len(user.data) > 0

# Create a new user
@app.post("/user")
def create_user(user: User):
    try:
        # Convert email to lowercase
        user_email = user.email.lower()
        # Hash password
        hased_password = user.password

        # Check if user already exists
        if user_exists(value=user_email):
            return {"message": "User already exists"}

        # Add user to users table
        user = supabase.from_("users")\
            .insert({"name": user.name, "email": user_email, "password": hased_password})\
            .execute()

        # Check if user was added
        if user:
            return {"message": "User created successfully"}
        else:
            return {"message": "User creation failed"}
    except Exception as e:
        print("Error: ", e)
        return {"message": "User creation failed"}

# Retrieve a user
@app.get("/user")
def get_user(user_id: Union[str, None] = None):
    try:
        if user_id:
            user = supabase.from_("users")\
                .select("id", "name", "email")\
                .eq("id", user_id)\
                .execute()

            if user:
                return user
        else:
            users = supabase.from_("users")\
                .select("id", "email", "name")\
                .execute()
            if users:
                return users
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "User not found"}


#logging
@app.post("/user/logging")
async def logging_user(user: UserLogging):
    try:
        # Convert email to lowercase
        user_email = user.email.lower()

        # Check if user already exists
        if user_exists(value=user_email):
            user_from_db = supabase.from_("users").select("*").eq('email', user_email).execute()
            print(user.password)
            if user_from_db.data[0]["password"] == user.password:            
               return {"message": "User Authenticated"}
            else:
                raise HTTPException(status_code=404, detail="email or password error")

    except Exception as e:
        print("Error: ", e)
        return {"message": "User authentication failed"}