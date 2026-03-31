# 📘 BookMyTable — Restaurant Booking Platform

BookMyTable is a full‑stack restaurant reservation system built with **Django**, designed to deliver a clean, modern, and mobile‑friendly booking experience.  
Users can browse restaurants, make reservations, manage their bookings, and receive clear status updates (Pending / Accepted / Rejected).  
Admins can manage restaurants, profiles and bookings through a dashboard.

This project demonstrates a CRUD system, clean architecture, and realistic booking workflows.

---

## 🚀 Live Demo


---

## 🎯 Project Goals

- Provide a smooth, intuitive booking experience for users  
- Give restaurant owners/admins full control over reservations  
- Deliver a premium, cohesive UI across all pages  
- Implement realistic booking workflows (Pending → Accepted/Rejected)  
- Ensure mobile‑first responsiveness  
- Meet Code Institute assessment requirements with clean documentation and testing  

---

## 🧩 Features

### 👤 User Features
- Create an account & log in  
- Browse restaurants with images and descriptions  
- Make a reservation with:
  - Date picker  
  - Time picker  
  - Party size  
  - Special requests  
- View all bookings in a clean dashboard  
- Edit or cancel bookings  
- See booking status:
  - **Pending** (yellow)  
  - **Accepted** (green)  
  - **Rejected** (red)

### 🛠️ Admin Features
- Manage restaurants, tables, profiles, and bookings  
- Approve or reject bookings  
- Jazzmin‑styled admin panel for a modern dashboard experience  
- Filter bookings by status  
- Edit bookings directly from the list view  

### 🎨 UI/UX Features
- Soft gradient backgrounds  
- Clean card‑based layout  
- Mobile‑first responsive design  
- Clear visual hierarchy  
- Status badges for instant clarity  
- Native date/time pickers for frictionless booking  
- Consistent Bootstrap styling  

---

## 🏗️ Technologies Used

| Area | Technology |
|------|------------|
| Backend | Django 6, Python |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite (development) |
| Admin UI | Jazzmin |
| Deployment | Heroku |
| Version Control | Git & GitHub |

---

## 📚 User Stories

### As a user:
- I want to browse restaurants so I can choose where to eat  
- I want to make a booking easily  
- I want to see my bookings in one place  
- I want to edit or cancel a booking  
- I want to know if my booking is confirmed  

### As an admin:
- I want to view all bookings  
- I want to approve or reject bookings  
- I want to manage restaurants and tables  
- I want a clean dashboard to work efficiently  

---

## 🗂️ Database Models

### Booking
- user  
- restaurant  
- date  
- time  
- party_size  
- special_requests  
- **status** (pending / accepted / rejected)

### Restaurant
- name  
- description  
- image  
- location  

### Profile
- user  
- phone  
- preferences  

---

## 🔄 Booking Workflow

1. User submits a booking → **Pending**  
2. Admin reviews booking in Jazzmin admin  
3. Admin sets status to:
   - **Accepted**  
   - **Rejected**  
4. User sees updated status in “My Bookings”

This mirrors real restaurant workflows and improves UX clarity.

---

## 🧪 Testing

### Manual Testing
- All forms tested for validation  
- Booking creation, editing, and deletion tested  
- Status updates tested in admin  
- Navigation tested on mobile and desktop  
- Time picker and date picker verified  
- 404 and 500 pages tested  

### Automated Testing


---

## 🛠️ Bugs & Fixes

### Static files not loading (Jazzmin)
- Fixed by correcting `STATIC_URL` to `/static/`  
- Added `STATIC_ROOT` and ran `collectstatic`  
- Ensured `DEBUG=True` for development  

### Time format confusion
- Replaced text input with native `<input type="time">`  
- Added widget in Django form  

### Admin theme conflict
- Removed Django Suit (incompatible with Django 6)  
- Installed Jazzmin instead  

---

## 📦 Installation

```bash
git clone <repo-url>
cd restaurant-booking
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Deployment

Credits

