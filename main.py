from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from datetime import date
from typing import List, Dict

from database import engine, init_db
from models import Expense

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize DB
init_db()

# Helper: aggregate summaries
def summarize(expenses: List[Expense]) -> Dict:
    by_category = {}
    by_month = {}
    total = 0.0

    for e in expenses:
        total += e.amount
        by_category[e.category] = by_category.get(e.category, 0) + e.amount

        ym = f"{e.expense_date.year}-{e.expense_date.month:02d}"
        by_month[ym] = by_month.get(ym, 0) + e.amount

    # Sorted month labels
    month_labels = sorted(by_month.keys())
    month_values = [by_month[m] for m in month_labels]

    # Category labels/values
    cat_labels = list(by_category.keys())
    cat_values = [by_category[c] for c in cat_labels]

    return {
        "total": total,
        "cat_labels": cat_labels,
        "cat_values": cat_values,
        "month_labels": month_labels,
        "month_values": month_values,
    }

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    with Session(engine) as session:
        expenses = session.exec(select(Expense).order_by(Expense.expense_date.desc(), Expense.id.desc())).all()
    summary = summarize(expenses)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "expenses": expenses,
            "summary": summary,
        },
    )

@app.post("/add", response_class=RedirectResponse)
def add_expense(
    title: str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    expense_date: date = Form(...),
):
    with Session(engine) as session:
        e = Expense(title=title, amount=amount, category=category, expense_date=expense_date)
        session.add(e)
        session.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{expense_id}", response_class=RedirectResponse)
def delete_expense(expense_id: int):
    with Session(engine) as session:
        e = session.get(Expense, expense_id)
        if e:
            session.delete(e)
            session.commit()
    return RedirectResponse(url="/", status_code=303)