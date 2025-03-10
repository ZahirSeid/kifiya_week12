from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import get_messages, create_message
from schemas import TelegramMessage, TelegramMessageCreate
from models import Base
from database import engine

# Initialize FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to the Telegram Messages API"}

@app.get("/messages/", response_model=list[TelegramMessage])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Read messages with optional skip and limit query parameters"""
    messages = get_messages(db, skip=skip, limit=limit)
    return messages

@app.post("/messages/", response_model=TelegramMessage, status_code=201)
def create_message_endpoint(message_data: TelegramMessageCreate, db: Session = Depends(get_db)):
    """Create a new message"""
    try:
        new_message = create_message(db, message_data)
        return new_message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

