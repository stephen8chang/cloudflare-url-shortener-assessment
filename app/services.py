import random
import string
from datetime import datetime
from sqlalchemy.orm import Session
from .models import ShortURL
from .redis_client import redis_client

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def create_short_url(db: Session, long_url: str, expires_at: datetime = None):
    short_code = generate_short_code()

    while db.query(ShortURL).filter(ShortURL.short_code == short_code).first():
        short_code = generate_short_code()

    short_url = ShortURL(short_code=short_code, long_url=long_url, expires_at=expires_at)
    db.add(short_url)
    db.commit()
    db.refresh(short_url)
    return short_url

def get_long_url(db: Session, short_code: str):
    cached_url = redis_client.get(short_code)
    if cached_url:
        return cached_url

    url_entry = db.query(ShortURL).filter(ShortURL.short_code == short_code).first()
    
    if url_entry:
        redis_client.set(short_code, url_entry.long_url, ex=86400)
        return url_entry.long_url
    return None

def increment_visit_count(db: Session, short_code: str):
    db.query(ShortURL).filter(ShortURL.short_code == short_code).update(
        {"visit_count": ShortURL.visit_count + 1}
    )
    db.commit()
