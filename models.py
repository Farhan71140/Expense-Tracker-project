from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field

class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    amount: float
    category: str  # e.g., "Food", "Travel", "Shopping", "Stock", "Delivery"
    expense_date: date