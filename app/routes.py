from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .services import create_short_url, get_long_url, increment_visit_count
from .schemas import ShortenRequest, ShortenResponse
from .models import ShortURL
from .redis_client import redis_client

router = APIRouter()

@router.post("/shorten", response_model=ShortenResponse)
def shorten_url(request: ShortenRequest, db: Session = Depends(get_db)):
    short_url = create_short_url(db, request.long_url)
    return {"short_url": f"http://localhost:8000/{short_url.short_code}"}

@router.get("/{short_url}")
def redirect_url(short_url: str, db: Session = Depends(get_db)):
    long_url = get_long_url(db, short_url)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    increment_visit_count(db, short_url)
    return {"redirect_to": long_url}

@router.delete("/{short_url}")
def delete_short_url(short_url: str, db: Session = Depends(get_db)):
    db.query(ShortURL).filter(ShortURL.short_code == short_url).delete()
    db.commit()
    redis_client.delete(short_url)
    return {"message": "Short URL deleted"}
