from sqlalchemy.orm import Session
from models import TelegramMessage
from schemas import TelegramMessageCreate

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve messages from the database"""
    return db.query(TelegramMessage).offset(skip).limit(limit).all()

def create_message(db: Session, message: TelegramMessageCreate):
    """Create a new message in the database"""
    db_message = TelegramMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
