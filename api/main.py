import bcrypt
from fastapi import FastAPI
from app.models import User
from db.supabase import create_supabase_client

app = FastAPI()

# Initialize supabase client
supabase = create_supabase_client()

def user_exists(key: str = "email", value: str = None):
    user = supabase.from_("users").select("*").eq(key, value).execute()
    return len(user.data) > 0

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
