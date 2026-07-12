-- EcoSphere Database Seed Data
-- 3 rows in every table, inserted in dependency order

USE ecosphere;

SET FOREIGN_KEY_CHECKS = 0;

-- ============================================================
-- CORE / ORG TABLES
-- ============================================================

-- departments (head_employee_id left NULL for now, updated after employees exist)
INSERT INTO departments (name, code, parent_department_id, employee_count, status) VALUES
('Engineering', 'ENG', NULL, 2, 'Active'),
('Human Resources', 'HR', NULL, 2, 'Active'),
('Marketing', 'MKT', NULL, 1, 'Active');

-- employees
INSERT INTO employees (department_id, name, email, role, xp_points, join_date, status) VALUES
(1, 'Aditi Rao', 'aditi.rao@ecosphere.com', 'Department Manager', 250, '2024-01-15', 'Active'),
(1, 'Rahul Mehta', 'rahul.mehta@ecosphere.com', 'Employee', 120, '2024-03-10', 'Active'),
(2, 'Sneha Kapoor', 'sneha.kapoor@ecosphere.com', 'Sustainability Officer', 400, '2023-11-05', 'Active'),
(2, 'Vikram Singh', 'vikram.singh@ecosphere.com', 'Compliance Officer', 180, '2024-02-20', 'Active'),
(3, 'Priya Nair', 'priya.nair@ecosphere.com', 'Employee', 90, '2024-05-12', 'Active');

-- Now update departments with their head employees
UPDATE departments SET head_employee_id = 1 WHERE code = 'ENG';
UPDATE departments SET head_employee_id = 3 WHERE code = 'HR';
UPDATE departments SET head_employee_id = 5 WHERE code = 'MKT';

-- ============================================================
-- MASTER DATA
-- ============================================================

-- categories
INSERT INTO categories (name, type, status) VALUES
('Community Cleanup', 'CSR_ACTIVITY', 'Active'),
('Energy Reduction', 'CHALLENGE', 'Active'),
('Water Conservation', 'CHALLENGE', 'Active');

-- emission_factor
INSERT INTO emission_factor (name, unit, co2e_value, source_type, status) VALUES
('Office Electricity', 'kWh', 0.4500, 'Expense', 'Active'),
('Company Vehicle Fuel', 'litre', 2.3100, 'Fleet', 'Active'),
('Business Travel Flights', 'km', 0.1500, 'Purchase', 'Active');

-- product_esg_profile
INSERT INTO product_esg_profile (product_name, emission_factor_id, esg_rating, notes) VALUES
('Recycled Paper Notebooks', 1, 'A', 'Sourced from certified recycled paper suppliers'),
('Standard Office Printer', 2, 'C', 'High energy consumption model, replacement planned'),
('Eco Laptop Stand', 3, 'B', 'Made from 80% recycled aluminum');

-- environmental_goal
INSERT INTO environmental_goal (department_id, metric_type, target_value, current_value, deadline, status) VALUES
(1, 'CO2 Reduction (kg)', 500.00, 120.00, '2026-12-31', 'Active'),
(2, 'Paper Usage Reduction (%)', 30.00, 10.00, '2026-09-30', 'Active'),
(3, 'Water Usage Reduction (%)', 20.00, 5.00, '2026-11-30', 'Active');

-- esg_policy
INSERT INTO esg_policy (title, description, document_url, version, status, effective_date) VALUES
('Remote Work Carbon Policy', 'Guidelines for reducing emissions from remote work setups', 'https://example.com/policies/remote-work.pdf', '1.0', 'Active', '2025-01-01'),
('Vendor Sustainability Standards', 'Minimum ESG requirements for third-party vendors', 'https://example.com/policies/vendor-esg.pdf', '2.1', 'Active', '2025-06-01'),
('Diversity & Inclusion Policy', 'Company-wide standards for workplace diversity and inclusion', 'https://example.com/policies/diversity.pdf', '1.0', 'Draft', '2026-10-01');

-- badges
INSERT INTO badges (name, description, unlock_rule, icon_url, status) VALUES
('Eco Starter', 'Awarded for earning your first 100 XP', JSON_OBJECT('type', 'xp_total', 'value', 100), 'https://example.com/icons/eco-starter.png', 'Active'),
('Green Champion', 'Awarded for completing 5 challenges', JSON_OBJECT('type', 'challenges_completed', 'value', 5), 'https://example.com/icons/green-champion.png', 'Active'),
('Consistency King', 'Awarded for logging activity 7 days in a row', JSON_OBJECT('type', 'streak_days', 'value', 7), 'https://example.com/icons/consistency-king.png', 'Active');

-- rewards
INSERT INTO rewards (name, description, points_required, stock, status) VALUES
('Extra Day Off', 'Redeem for one additional paid day off', 500, 10, 'Active'),
('Eco-Friendly Water Bottle', 'Reusable stainless steel water bottle', 150, 50, 'Active'),
('Company Branded Tote Bag', 'Reusable canvas tote bag with EcoSphere logo', 80, 100, 'Active');

-- ============================================================
-- JUNCTION TABLES
-- ============================================================

-- employee_badges
INSERT INTO employee_badges (employee_id, badge_id, awarded_at) VALUES
(1, 1, '2024-06-01 10:00:00'),
(3, 2, '2024-08-15 14:30:00'),
(5, 3, '2026-06-20 09:15:00');

-- reward_redemptions
INSERT INTO reward_redemptions (employee_id, reward_id, points_spent, status) VALUES
(1, 2, 150, 'Fulfilled'),
(3, 1, 500, 'Pending'),
(2, 3, 80, 'Fulfilled');

-- ============================================================
-- TRANSACTIONAL DATA
-- ============================================================

-- carbon_transaction
INSERT INTO carbon_transaction (department_id, emission_factor_id, source_type, source_record_id, quantity, co2e_calculated, calculation_mode) VALUES
(1, 1, 'Expense', NULL, 1200.0000, 540.0000, 'AUTO'),
(2, 2, 'Fleet', NULL, 85.5000, 197.5050, 'AUTO'),
(3, 3, 'Purchase', NULL, 450.0000, 67.5000, 'MANUAL');

-- csr_activity
INSERT INTO csr_activity (title, category_id, department_id, description, date, status) VALUES
('Beach Cleanup Drive', 1, 1, 'Team volunteer event to clean up the local beach', '2026-08-15', 'Active'),
('Tree Plantation Day', 1, 2, 'Planting saplings in the community park', '2026-09-01', 'Draft'),
('Recycling Awareness Workshop', 1, 3, 'Internal workshop teaching proper recycling practices', '2026-09-20', 'Draft');

-- employee_participation
INSERT INTO employee_participation (employee_id, activity_id, proof_url, approval_status, points_earned, completion_date) VALUES
(2, 1, 'https://example.com/proof/beach-cleanup-rahul.jpg', 'Approved', 50, '2026-08-15'),
(4, 1, 'https://example.com/proof/beach-cleanup-vikram.jpg', 'Pending', 0, NULL),
(5, 3, NULL, 'Pending', 0, NULL);

-- challenge
INSERT INTO challenge (title, category_id, description, xp, difficulty, evidence_required, deadline, status) VALUES
('Cut Energy Use by 10%', 2, 'Reduce your workstation energy usage by 10% this month', 100, 'Medium', TRUE, '2026-08-31', 'Active'),
('Zero Waste Week', 2, 'Produce zero non-recyclable waste for one full week', 150, 'Hard', TRUE, '2026-09-15', 'Draft'),
('Reduce Water Usage by 15%', 3, 'Track and reduce your personal water consumption at the office', 120, 'Medium', TRUE, '2026-10-15', 'Active');

-- challenge_participation
INSERT INTO challenge_participation (challenge_id, employee_id, progress, proof_url, approval_status, xp_awarded) VALUES
(1, 2, 60, 'https://example.com/proof/energy-challenge-rahul.jpg', 'Pending', 0),
(1, 4, 100, 'https://example.com/proof/energy-challenge-vikram.jpg', 'Approved', 100),
(3, 1, 40, NULL, 'Pending', 0);

-- policy_acknowledgement
INSERT INTO policy_acknowledgement (policy_id, employee_id, status) VALUES
(1, 1, 'Acknowledged'),
(1, 2, 'Pending'),
(2, 3, 'Acknowledged');

-- audit
INSERT INTO audit (department_id, title, description, auditor, status, date) VALUES
(1, 'Q3 Environmental Compliance Audit', 'Routine quarterly audit of environmental practices', 'Sneha Kapoor', 'Completed', '2026-07-01'),
(2, 'HR Policy Compliance Review', 'Review of HR department policy adherence', 'Vikram Singh', 'Scheduled', '2026-08-20'),
(3, 'Marketing Sustainability Review', 'Initial ESG baseline review for the Marketing department', 'Sneha Kapoor', 'Scheduled', '2026-09-10');

-- compliance_issue
INSERT INTO compliance_issue (audit_id, department_id, severity, description, owner_employee_id, due_date, status) VALUES
(1, 1, 'Medium', 'Missing documentation for waste disposal process', 1, '2026-08-01', 'Open'),
(NULL, 2, 'Low', 'Minor delay in policy acknowledgement tracking', 3, '2026-08-10', 'Open'),
(3, 3, 'Low', 'Marketing materials not yet reviewed for sustainability claims', 5, '2026-09-25', 'Open');

-- department_score
INSERT INTO department_score (department_id, environmental_score, social_score, governance_score, total_score, period) VALUES
(1, 78.50, 82.00, 75.00, 78.50, '2026-Q2'),
(2, 65.00, 90.00, 88.00, 81.00, '2026-Q2'),
(3, 55.00, 70.00, 60.00, 61.67, '2026-Q2');

SET FOREIGN_KEY_CHECKS = 1;