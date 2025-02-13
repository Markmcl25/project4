# Event Planner

![Display 1](static/images/readme/display1.jpg)
![Display 2](static/images/readme/display2.jpg)
![Display 3](static/images/readme/display3.jpg)
![Display 3](static/images/readme/darkmode.jpg)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [User Stories](#user-stories)
- [Technologies Used](#technologies-used)
- [Data Model](#data-model)
- [Deployment](#deployment)
- [Testing](#testing)
- [Bugs and Fixes](#bugs-and-fixes)
- [Future Enhancements](#future-enhancements)

## Project Overview
The **Event Planner** is a full-stack web application designed to help users create, manage, and discover events. It supports role-based access control, allowing event creators to manage their events, while general users can browse and register for events.

## Features
- User authentication (signup, login, logout)
- Role-based access (admin, event creators, regular users)
- CRUD functionality for events (Create, Read, Update, Delete)
- Dashboard for managing events
- Event filtering and search
- Responsive design
- Deployed on Heroku

## User Stories
### Epic: Event Management
- **As a user**, I want to create an event so that I can invite people.
- **As an admin**, I want to manage all events to ensure proper moderation.
- **As an event creator**, I want to edit or delete my events.

![User stories](static/images/readme/userstories.jpg)

### User Acceptance Criteria
- Users can create, update, and delete their events.
- Events are displayed with details including title, date, location, and description.
- Only event creators or admins can edit/delete events.

## Technologies Used
- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Django
- **Database:** PostgreSQL (Heroku Postgres)
- **Deployment:** Heroku
- **Version Control:** Git, GitHub

## Data Model
### Event Model
- `title` (CharField)
- `description` (TextField)
- `date` (DateTimeField)
- `location` (CharField)
- `category` (CharField)
- `image` (ImageField)
- `creator` (ForeignKey to User)

### ERD Diagram
![Flow chart](static/images/readme/flow_chart.jpg)

## Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/Markmcl25/project4.git
   cd project4
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables:
   - `SECRET_KEY`
   - `DATABASE_URL`
   - `CLOUDINARY_URL`
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Deploy to Heroku:
   ```bash
   heroku create event-planner01
   git push heroku main
   heroku run python manage.py migrate
   ```

![Heroku](static/images/readme/heroku.jpg)   

## Testing
- **Unit Tests:** Cover models, views, and forms.
- **Manual Testing:**
  - Event creation, editing, deletion.
  - User authentication flows.
  - Role-based access checks.

![Tests](static/images/readme/tests.jpg) 

## Bugs and Fixes
- **Issue:** Event deletion not reflecting immediately.
  - **Fix:** Added AJAX refresh.
- **Issue:** Image upload errors on Heroku.
  - **Fix:** Configured Cloudinary settings.

## Checks on Validators  
Base.html check
![Base](static/images/readme/base.checker.jpg)
Dashboard.html
![Dash](static/images/readme/dash.sc.jpg)
Event list
![Event](static/images/readme/event-sc.jpg)

## Future Enhancements
- Event RSVP functionality
- User profile pages
- Integration with calendar APIs


