
#  CSCV337 HW5



##  File Structure

```
news_project/
├── news_app/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── article.html
│   │   ├── base.html
│   ├── static/
│   │   ├── styles.css
│   │   ├── script.js
│   ├── views.py
│   ├── urls.py
│   └── ...
├── data/
│   ├── articles.csv
│   ├── visualcontent.csv
├── manage.py
```

---



## ⚙️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies:**
   Make sure Python 3 and Django are installed.
   ```bash
   pip install django
   ```

3. **Run migrations & load CSV:**
   ```bash
   python manage.py migrate
   python manage.py loaddata your_json_file_if_any  # or custom CSV loader
   ```

4. **Create a superuser (for admin tools):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   - Go to: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

---

