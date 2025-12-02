# 💼 Expense Tracker

- 📖 **Overview**: A full‑stack web application built with **FastAPI** ⚡, **SQLModel** 🗂️, and **Chart.js** 📊 to help users record, manage, and visualize their daily expenses in a simple yet powerful way.  

- 🚀 **Features**:  
  - Add, edit, and delete expense entries ✍️  
  - View total and category‑wise summaries 📊  
  - Analyze spending patterns with interactive charts 🎨  
  - Responsive frontend with HTML, CSS, and Bootstrap 🌐  
  - Lightweight SQLite database integration 🧱  

- 🛠️ **Tech Stack**:  
  - Backend: FastAPI ⚡, SQLModel 🗂️  
  - Frontend: HTML, CSS, Bootstrap 🎨, Chart.js 📈  
  - Database: SQLite 🧱  
  - Environment: Python 3.x 🐍, Virtualenv 🧪  

- 📂 **Project Structure**:  
  - `main.py` → FastAPI app and routing  
  - `models.py` → SQLModel definitions  
  - `database.py` → Database engine setup  
  - `templates/` → HTML files  
  - `static/` → CSS and JS assets  
  - `requirements.txt` → Dependencies  
  - `.gitignore` 🚫 → Excludes `.venv/`, `__pycache__/`, and `expenses.db`  
  - `README.md` → Project documentation  

- ⚙️ **Setup Instructions**:  
  1. Clone the repository 🔽  
     ```bash
     git clone https://github.com/your-username/expense-tracker.git
     cd expense-tracker
     ```  
  2. Create and activate virtual environment 🧪  
     ```bash
     python -m venv .venv
     source .venv/Scripts/activate   # Windows
     ```  
  3. Install dependencies 📦  
     ```bash
     pip install -r requirements.txt
     ```  
  4. Run the application ▶️  
     ```bash
     uvicorn main:app --reload
     ```  
  5. Open in browser 🌐 → `http://127.0.0.1:8000`  
  6. Access charts 📊 → `http://127.0.0.1:8000/summary`  

- 🔮 **Future Improvements**:  
  - Add user authentication 🔒  
  - Deploy to cloud ☁️ (Heroku, Render, Azure)  
  - Enhance mobile responsiveness 📱  
  - Enable CSV/Excel export 📤  

- 👨‍💻 **Author**:  
  - **Mohammed Farhan Uddin**  
  - Aspiring Full‑Stack Python Developer | Owner of Madam Choice Footwear  
  - 📧 farhanuddin0516@gmail.com  

- 📝 **License**: MIT License — free to use and modify ✅
