# app/database.py
from sqlmodel import create_engine, Session, SQLModel
from app.config import settings

# Create the SQLAlchemy engine for MySQL
# echo=True is helpful during a hackathon to see the SQL queries in your terminal
engine = create_engine(
    settings.DATABASE_URL, 
    echo=False, 
    pool_pre_ping=True
)

def init_db():
    """Initializes the database and creates all tables defined in models."""
    # This will be called on app startup in main.py
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency for providing a database session to routes."""
    with Session(engine) as session:
        yield session