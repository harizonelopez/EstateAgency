# PropertyPlus – Real Estate Management Website

**PropertyPlus** is a Django-based real estate website designed to provide a modern and user-friendly platform for showcasing properties, connecting clients with real estate agents, and managing property enquiries.

The platform allows visitors to explore available properties, learn about real estate services, view agent profiles, and submit enquiries. The administrative interface provides a central place to manage website content and property-related information.

## Features

### Property Management
- Display available properties for sale and rent.
- Browse detailed property information.
- Organize listings by property type.
- Display property images and galleries.
- Highlight featured properties.
- Manage property availability.

### Agent Management
- Display real estate agent profiles.
- View agent biographies and professional experience.
- Showcase achievements and areas of specialization.
- Display contact and social media information.
- Manage agent profiles through Django Admin.

### Enquiries and Contact
- Submit general enquiries.
- Request property viewings.
- Send buying and renting enquiries.
- Associate enquiries with specific properties.
- Validate submitted contact information.
- Track enquiry status through the administrative interface.
- Send email notifications using Django's email framework.

### Website Content
- Homepage with property highlights.
- About page.
- Services page and individual service details.
- Agent profiles and details.
- Client testimonials managed through the database.
- Responsive navigation and footer.

### Administration
- Django's built-in administrative interface.
- Manage property listings and images.
- Manage real estate agents.
- Manage services and testimonials.
- Review and update client enquiries.

## Technology Stack

| Technology       | Purpose                          |
|------------------|----------------------------------|
| Python           | Backend programming language     |
| Django 6.1.3     | Web application framework        |
| SQLite           | Development database             |
| HTML5            | Page structure                   |
| CSS3             | Custom styling                   |
| Bootstrap        | Responsive frontend framework    |
| JavaScript       | Frontend interactions            |
| Pillow           | Image processing                 |
| Python Dotenv    | Environment variable management  |
| Django Email     | Email notifications              |

## Project Structure

```text
EstateAgency/
│
├── agents/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── enquiries/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── properties/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
├── assets/
├── media/
├── forms/
├── .gitignore
├── manage.py
├── requirements.txt
├── secrets.env
└── README.md
```

*The structure above highlights the main application directories.*

## Running the Application

### 1. Prerequisites

- Python 3.12.
- Git.

### 2. Clone the Repository

```bash
 git clone https://github.com/harizonelopez/EstateAgency.git
```

Navigate into the project:

```bash
 cd EstateAgency
```

### 3. Create a Virtual Environment

```bash
 python -m venv .env
```

Activate it on Windows:

```bash
 .env\Scripts\activate
```

OR

Activate on Mac:

```bash
 source .env/bin/activate
```

### 4. Install Dependencies

```bash
 python -m pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a file named `secrets.env` in the project root directory & add the following:

```env
 SECRET_KEY=`your_django_secret_key`
 EMAIL_HOST_USER=`your_email@gmail.com`
 EMAIL_HOST_PASSWORD=`your_email_app_password`
 AGENCY_EMAIL=`your_agency_email@gmail.com`
```

*Replace the quoted values with your own credentials.*

### 6. Apply Database Migrations

```bash
 python manage.py makemigrations
 python manage.py migrate
```

### 7. Create an Administrator Account

```bash
 python manage.py createsuperuser
```

*Follow the prompts to create an administrator account for django admin management.*

### 8. Start the Development Server

```bash
 python manage.py runserver
```

Open the URL in the browser:

```text
 http://127.0.0.1:8000
```

Access the Django admin panel:

```text
 http://127.0.0.1:8000/admin
```

## Environment Configuration

The application uses environment variables for sensitive configuration, including:

- Django secret key.
- Email account credentials.
- Agency notification email address.

The development database uses SQLite, which Django creates as `db.sqlite3` after migrations.

Uploaded property and agent images are stored in the media directory.

## Security Notes

Before deploying the application:

- Set `DEBUG = False`.
- Configure `ALLOWED_HOSTS`.
- Use a secure production `SECRET_KEY`.
- Keep credentials in environment variables.
- Configure HTTPS.
- Configure production static and media file serving.
- Use an appropriate production database.

## Future Improvements

Potential improvements include:

- Client accounts and enquiry tracking.
- Online property viewing scheduling.
- Enhanced analytics for administrators.

## Author

**Harison Onyango**

Computer Science Student | Software Developer

---

*PropertyPlus EstateAgency – Making property discovery and real estate connections easier.*