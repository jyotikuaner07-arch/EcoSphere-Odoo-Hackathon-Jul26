"""Populate EcoSphere with demo data for hackathon presentations."""

from datetime import date, timedelta
from decimal import Decimal

from sqlmodel import Session, select

from app.auth.security import hash_password
from app.constants.enums import (
    CategoryType,
    ChallengeDifficulty,
    ChallengeStatus,
    CsrActivityStatus,
    GenericStatus,
    PolicyStatus,
    SourceType,
    UserRole,
)
from app.database import engine, init_db
from app.models.badge import Badge
from app.models.category import Category
from app.models.challenge import Challenge
from app.models.csr_activity import CsrActivity
from app.models.department import Department
from app.models.emission_factor import EmissionFactor
from app.models.environmental_goal import EnvironmentalGoal
from app.models.policy import Policy
from app.models.reward import Reward
from app.models.settings import OrganizationSettings
from app.models.user import User


def seed() -> None:
    init_db()

    with Session(engine) as session:
        if session.exec(select(Department)).first():
            print("Database already seeded — skipping.")
            return

        # 1. Departments (no head yet — circular FK with employees)
        mfg = Department(name="Manufacturing", code="MFG", employee_count=120)
        log = Department(name="Logistics", code="LOG", employee_count=45)
        hr = Department(name="Human Resources", code="HR", employee_count=30)
        session.add_all([mfg, log, hr])
        session.commit()
        session.refresh(mfg)
        session.refresh(log)
        session.refresh(hr)

        # 2. Users (one per role for demo login)
        users = [
            User(
                name="Admin User",
                email="admin@ecosphere.com",
                password_hash=hash_password("admin123"),
                department_id=mfg.id,
                role=UserRole.ADMIN,
                xp_points=0,
            ),
            User(
                name="Sustainability Officer",
                email="sustainability@ecosphere.com",
                password_hash=hash_password("sustain123"),
                department_id=mfg.id,
                role=UserRole.SUSTAINABILITY_OFFICER,
            ),
            User(
                name="Compliance Officer",
                email="compliance@ecosphere.com",
                password_hash=hash_password("comply123"),
                department_id=hr.id,
                role=UserRole.COMPLIANCE_OFFICER,
            ),
            User(
                name="Department Manager",
                email="manager@ecosphere.com",
                password_hash=hash_password("manager123"),
                department_id=mfg.id,
                role=UserRole.DEPARTMENT_MANAGER,
            ),
            User(
                name="Demo Employee",
                email="employee@ecosphere.com",
                password_hash=hash_password("employee123"),
                department_id=mfg.id,
                role=UserRole.EMPLOYEE,
                xp_points=100,
            ),
        ]
        session.add_all(users)
        session.commit()

        admin = session.exec(select(User).where(User.email == "admin@ecosphere.com")).one()
        mfg.head_employee_id = admin.id
        session.add(mfg)
        session.commit()

        # 3. Categories
        csr_cat = Category(name="Environmental Volunteering", type=CategoryType.CSR_ACTIVITY)
        challenge_cat = Category(name="Energy Reduction", type=CategoryType.CHALLENGE)
        session.add_all([csr_cat, challenge_cat])
        session.commit()
        session.refresh(csr_cat)
        session.refresh(challenge_cat)

        # 4. Emission factors
        factors = [
            EmissionFactor(
                name="Grid Electricity",
                unit="kWh",
                co2e_value=Decimal("0.4500"),
                source_type=SourceType.MANUFACTURING,
            ),
            EmissionFactor(
                name="Diesel Fleet",
                unit="litre",
                co2e_value=Decimal("2.6800"),
                source_type=SourceType.FLEET,
            ),
            EmissionFactor(
                name="Office Supplies",
                unit="kg",
                co2e_value=Decimal("1.2000"),
                source_type=SourceType.PURCHASE,
            ),
        ]
        session.add_all(factors)
        session.commit()

        # 5. Environmental goals
        session.add(
            EnvironmentalGoal(
                department_id=mfg.id,
                metric_type="Carbon Reduction (kg CO2e)",
                target_value=Decimal("5000.00"),
                current_value=Decimal("1200.00"),
                deadline=date.today() + timedelta(days=180),
            )
        )

        # 6. CSR activities
        activities = [
            CsrActivity(
                title="Tree Planting Drive",
                category_id=csr_cat.id,
                department_id=mfg.id,
                description="Plant 500 saplings in the local community.",
                date=date.today() + timedelta(days=14),
                points=75,
                status=CsrActivityStatus.ACTIVE,
            ),
            CsrActivity(
                title="Beach Cleanup",
                category_id=csr_cat.id,
                department_id=log.id,
                description="Coastal cleanup with local NGO partners.",
                points=50,
                status=CsrActivityStatus.ACTIVE,
            ),
        ]
        session.add_all(activities)

        # 7. Challenges
        challenges = [
            Challenge(
                title="Reduce Office Energy by 10%",
                category_id=challenge_cat.id,
                description="Track and reduce energy usage for 30 days.",
                xp=200,
                difficulty=ChallengeDifficulty.MEDIUM,
                evidence_required=True,
                deadline=date.today() + timedelta(days=30),
                status=ChallengeStatus.ACTIVE,
            ),
            Challenge(
                title="Zero-Waste Week",
                category_id=challenge_cat.id,
                description="No single-use plastics for one week.",
                xp=150,
                difficulty=ChallengeDifficulty.EASY,
                status=ChallengeStatus.ACTIVE,
            ),
        ]
        session.add_all(challenges)

        # 8. Badges
        session.add_all(
            [
                Badge(
                    name="Green Starter",
                    description="Earn 100 XP",
                    unlock_rule={"type": "xp", "threshold": 100},
                    icon_url="/icons/green-starter.svg",
                ),
                Badge(
                    name="Challenge Champion",
                    description="Complete 3 challenges",
                    unlock_rule={"type": "completed_challenges", "threshold": 3},
                    icon_url="/icons/champion.svg",
                ),
            ]
        )

        # 9. Rewards
        session.add_all(
            [
                Reward(
                    name="Eco Water Bottle",
                    description="Stainless steel reusable bottle",
                    points_required=150,
                    stock=20,
                    status=GenericStatus.ACTIVE,
                ),
                Reward(
                    name="Extra Leave Day",
                    description="One bonus leave day",
                    points_required=500,
                    stock=5,
                    status=GenericStatus.ACTIVE,
                ),
            ]
        )

        # 10. Policies
        session.add(
            Policy(
                title="Code of Conduct",
                description="Company-wide ethical conduct policy.",
                version="1.0",
                status=PolicyStatus.ACTIVE,
                effective_date=date.today(),
            )
        )

        # 11. Organization settings (singleton)
        session.add(OrganizationSettings(id=1))

        session.commit()
        print("Seed complete. Demo logins:")
        print("  admin@ecosphere.com / admin123")
        print("  employee@ecosphere.com / employee123")


if __name__ == "__main__":
    seed()
