from sqlmodel import SQLModel, create_engine

# Define the SQLite database URL
DATABASE_URL = "sqlite:///./expenses.db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=False)

# Initialize the database
def init_db():
    from models import Expense  # Import your model here
    SQLModel.metadata.create_all(engine)