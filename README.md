# 📘 BookMyTable — Restaurant Booking Platform

BookMyTable is a full‑stack restaurant reservation system built with **Django**, designed to deliver a clean, modern, and mobile‑friendly booking experience.  
Users can browse restaurants, make reservations, manage their bookings, and receive clear status updates (Pending / Accepted / Rejected).  
Admins can manage restaurants, tables, and bookings through a polished Jazzmin‑styled dashboard.

This project demonstrates strong UX thinking, clean architecture, and realistic booking workflows.

---

# 🎯 Rationale & Target Audience

BookMyTable was created to solve a real‑world problem: small restaurants often lack a simple, intuitive online booking system.  
The target audience includes:

- **Restaurant customers** who want a fast, mobile‑friendly way to book a table  
- **Restaurant owners/admins** who need an easy way to manage reservations  
- **Users with accessibility needs**, thanks to clear navigation, semantic HTML, and responsive design  

The purpose of the application is immediately clear to new users:  
➡️ *Browse restaurants → Book a table → Manage your bookings.*

---

# 🧩 Features

## 👤 User Features

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

## 🛠️ Admin Features

- Manage restaurants, tables, profiles, and bookings  
- Approve or reject bookings  
- Jazzmin‑styled admin panel  
- Filter bookings by status  
- Edit bookings directly from the list view  

## 🎨 UX & Accessibility Features

BookMyTable follows key UX principles:

### **Information Hierarchy**
- Restaurant cards use clear headings, images, and spacing  
- Booking cards highlight the most important information first  
- Navigation is consistent across all pages  

### **User Control**
- Users initiate all actions (no autoplay, no pop‑ups)  
- Clear feedback after every action (booking created, updated, deleted)  
- Status badges give immediate clarity  

### **Consistency**
- Same layout structure across all pages  
- Consistent button styles, spacing, and typography  

### **Accessibility**
- Semantic HTML  
- High‑contrast buttons  
- Large tap targets on mobile  
- Native date/time pickers  
- Alt text on images  

---

# Screenshots

### Home Page:

![Homepage Screenshot](docs/screenshots/home-page.png)

### Restaurant list:

![Restaurant List Screenshot](docs/screenshots/restaurant-list.png)

### Booking From:

![Booking Form Screenshot](docs/screenshots/booking-form.png)

### My bookings Dashboard:

![My Bookings Screenshot](docs/screenshots/my-bookings.png)

### Admin Panel (Jazzmin):

![Admin Panel Screenshot](docs/screenshots/admin-panel.png)

---

# WIREFRAME 

Below is a simple wireframe representing the core user flow.
```
[ Homepage ]
      |
      v
[ Restaurant List ]
      |
      v
[ Restaurant Detail ]
      |
      v
[ Booking Form ]
      |
      v
[ Booking Confirmation ]
      |
      v
[ My Bookings Dashboard ]
```


---

# 🗂️ Database Schema

The application uses a relational database with the following structure:

## **Restaurant**
| Field | Type | Notes |
|-------|------|-------|
| id | PK | Auto |
| name | CharField | Required |
| description | TextField | |
| image | ImageField | |
| location | CharField | |

## **Booking**
| Field | Type | Notes |
|-------|------|-------|
| id | PK | Auto |
| user | FK → User | Required |
| restaurant | FK → Restaurant | Required |
| date | DateField | Required |
| time | TimeField | Required |
| party_size | IntegerField | Required |
| special_requests | TextField | Optional |
| status | CharField | pending/accepted/rejected |

## **Profile**
| Field | Type | Notes |
|-------|------|-------|
| user | OneToOne → User | Required |
| phone | CharField | Optional |
| preferences | TextField | Optional |

### **Schema Summary**
The schema is designed to support a realistic restaurant booking workflow, with clear relationships between users, restaurants, and bookings.  

---

# 🔄 Booking Workflow

1. User submits a booking → **Pending**  
2. Admin reviews booking in Jazzmin admin  
3. Admin sets status to:
   - **Accepted**  
   - **Rejected**  
4. User sees updated status in “My Bookings”

This mirrors real restaurant workflows and improves UX clarity.

---

# 🧪 Testing

## Manual Testing Procedure
A full manual testing table is included below:

| Feature | Test | Expected Result | Pass |
|--------|------|-----------------|------|
| Register | Submit valid form | Account created | ✔ |
| Login | Enter correct credentials | Redirect to home | ✔ |
| Create booking | Submit form | Booking saved as Pending | ✔ |
| Edit booking | Change details | Updated booking visible | ✔ |
| Cancel booking | Click cancel | Booking removed | ✔ |
| Admin approve | Change status | User sees Accepted | ✔ |
| Navigation | Click all links | No broken links | ✔ |
| Mobile layout | Resize window | Layout adapts | ✔ |

---

# 🧪 Code Validation

## **HTML** validated with W3C  

##  **CSS** validated with Jigsaw  

### Note: Bootstrap 5.3.2 CDN triggers several false‑positive errors in the W3C CSS validator due to modern CSS features not yet supported by the validator. These errors do not affect functionality and are unrelated to project code
 

---

# 🛠️ Version Control

- Git used throughout development  
- Small, descriptive commits for each feature  
- No large “dump” commits  
- Clear commit history showing development process  



---

# 🔐 Security Features

- Secret key stored in environment variable  
- DEBUG = False in production  
- No secrets committed to GitHub  
- User permissions enforced (only owners can edit/delete their bookings)  



---

# 📦 Installation

```bash
git clone <repo-url>
cd restaurant-booking
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

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

### Deployment

### Credits

