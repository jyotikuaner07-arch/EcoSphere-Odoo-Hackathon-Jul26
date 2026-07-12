# EcoSphere - ESG Management Platform

EcoSphere is an Environmental, Social, and Governance (ESG) management platform designed to help organizations track, measure, and improve their sustainability performance. It integrates operational data, employee engagement, and compliance activities into a unified dashboard while encouraging sustainability through gamification.

## Features

### Environmental
- Configure Emission Factors
- Calculate Carbon Emissions
- Department Carbon Tracking
- Sustainability Goals
- Environmental Dashboard

### Social
- CSR Activities
- Employee Participation
- Diversity Metrics
- Training Completion

### Governance
- ESG Policies
- Policy Acknowledgements
- Audits
- Compliance Issues

### Gamification
- Challenges (with full lifecycle: Draft → Active → Under Review → Completed/Archived)
- XP Points
- Badges (auto-awarded based on XP or completed challenges)
- Rewards (redeemable using earned XP)
- Leaderboards

### Quiz
- Sustainability quizzes with multiple-choice questions
- XP rewards for completing quizzes

### Settings & Administration
- Departments Management
- Category Management
- ESG Configuration
- Notification Settings

## Tech Stack

### Backend
- Python 3.10+
- FastAPI
- SQLModel
- SQLite (default, can use MySQL/PostgreSQL)

### Frontend
- React 18
- Vite
- Tailwind CSS
- Framer Motion
- Lucide React Icons
- Axios

## Installation

### Prerequisites
- Python 3.10+
- Node.js 18+
- npm or yarn

### Backend Setup
1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory using `.env.example` as a template:
```bash
cp .env.example .env
```

5. (Optional) Seed the database with sample data:
```bash
python seed.py
```

6. Start the backend server:
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at http://localhost:8000, and the API documentation is at http://localhost:8000/docs!

### Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file in the frontend directory using `.env.example` as a template:
```bash
cp .env.example .env
```

4. Start the frontend development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:5173 or the next available port!

## Default Credentials
When you seed the database with sample data, the following credentials are available:
- Admin: admin@ecosphere.com / admin123
- Employee: employee@ecosphere.com / employee123

## Project Structure

```
EcoSphere-Odoo-Hackathon-Jul26/
├── backend/
│   ├── app/
│   │   ├── auth/           # Authentication
│   │   ├── constants/      # Enum definitions
│   │   ├── core/           # Core functionality
│   │   ├── middleware/     # Middleware
│   │   ├── models/         # SQLModel models
│   │   ├── routers/        # API routers
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic
│   │   ├── utils/          # Utility functions
│   │   └── ...
│   ├── seed.py             # Database seeder
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── api/            # API configuration
│   │   ├── assets/         # Static assets
│   │   ├── components/     # React components
│   │   ├── constants/      # Constants and enums
│   │   ├── context/        # React context providers
│   │   ├── hooks/          # Custom hooks
│   │   ├── mocks/          # Mock data for development
│   │   ├── pages/          # React pages
│   │   └── ...
│   └── ...
└── README.md               # This file
```

## License
MIT
