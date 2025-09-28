from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(title="FastAPI Boilerplate", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    """Homepage route with Jinja2 template"""
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "title": "FastAPI Boilerplate"}
    )

@app.get("/profile/{username}")
async def user_profile(request: Request, username: str):
    """User profile page demonstrating Jinja2 template variables"""
    # Mock user data - in real app, this would come from database
    user_data = {
        "username": username,
        "full_name": f"{username.title()} Smith",
        "email": f"{username}@example.com",
        "joined_date": "2024-01-15",
        "posts_count": 42,
        "followers": 1337,
        "following": 256,
        "bio": f"Hello! I'm {username}. Welcome to my profile page.",
        "skills": ["Python", "FastAPI", "JavaScript", "React", "Docker"],
        "recent_posts": [
            {"title": "Getting Started with FastAPI", "date": "2024-09-25", "likes": 23},
            {"title": "Jinja2 Templates Guide", "date": "2024-09-20", "likes": 45},
            {"title": "Building REST APIs", "date": "2024-09-15", "likes": 67}
        ],
        "is_verified": username.lower() in ["admin", "john", "jane"]
    }
    
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "title": f"{user_data['full_name']} - Profile",
            "user": user_data,
            "page_title": "User Profile"
        }
    )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "FastAPI is running!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)