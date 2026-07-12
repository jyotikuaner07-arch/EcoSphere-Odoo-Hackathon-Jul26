-- EcoSphere Database Schema
-- MySQL 8.0
-- Tables ordered by dependency (safe to run top-to-bottom on a fresh database)

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `department_score`;
DROP TABLE IF EXISTS `compliance_issue`;
DROP TABLE IF EXISTS `audit`;
DROP TABLE IF EXISTS `policy_acknowledgement`;
DROP TABLE IF EXISTS `challenge_participation`;
DROP TABLE IF EXISTS `challenge`;
DROP TABLE IF EXISTS `employee_participation`;
DROP TABLE IF EXISTS `csr_activity`;
DROP TABLE IF EXISTS `reward_redemptions`;
DROP TABLE IF EXISTS `employee_badges`;
DROP TABLE IF EXISTS `rewards`;
DROP TABLE IF EXISTS `badges`;
DROP TABLE IF EXISTS `esg_policy`;
DROP TABLE IF EXISTS `environmental_goal`;
DROP TABLE IF EXISTS `product_esg_profile`;
DROP TABLE IF EXISTS `emission_factor`;
DROP TABLE IF EXISTS `categories`;
DROP TABLE IF EXISTS `employees`;
DROP TABLE IF EXISTS `departments`;

-- ============================================================
-- CORE / ORG TABLES
-- ============================================================

--
-- Table structure for table `departments`
--
CREATE TABLE `departments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `code` varchar(20) DEFAULT NULL,
  `head_employee_id` int DEFAULT NULL,
  `parent_department_id` int DEFAULT NULL,
  `employee_count` int DEFAULT '0',
  `status` enum('Active','Inactive') DEFAULT 'Active',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `employees`
--
CREATE TABLE `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `department_id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `role` enum('Admin','Sustainability Officer','Compliance Officer','Department Manager','Employee','Management') DEFAULT 'Employee',
  `xp_points` int DEFAULT '0',
  `join_date` date DEFAULT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `fk_emp_department` (`department_id`),
  CONSTRAINT `fk_emp_department` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Now that employees exists, add departments' self/head foreign keys
ALTER TABLE `departments`
  ADD KEY `fk_dept_parent` (`parent_department_id`),
  ADD KEY `fk_dept_head` (`head_employee_id`),
  ADD CONSTRAINT `fk_dept_head` FOREIGN KEY (`head_employee_id`) REFERENCES `employees` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `fk_dept_parent` FOREIGN KEY (`parent_department_id`) REFERENCES `departments` (`id`) ON DELETE SET NULL;

-- ============================================================
-- MASTER DATA (mostly static/config)
-- ============================================================

--
-- Table structure for table `categories`
--
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `type` enum('CSR_ACTIVITY','CHALLENGE') NOT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `emission_factor`
--
CREATE TABLE `emission_factor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `unit` varchar(50) NOT NULL,
  `co2e_value` decimal(10,4) NOT NULL,
  `source_type` enum('Purchase','Manufacturing','Expense','Fleet') NOT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `product_esg_profile`
--
CREATE TABLE `product_esg_profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(150) NOT NULL,
  `emission_factor_id` int NOT NULL,
  `esg_rating` varchar(10) DEFAULT NULL,
  `notes` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_pep_emission` (`emission_factor_id`),
  CONSTRAINT `fk_pep_emission` FOREIGN KEY (`emission_factor_id`) REFERENCES `emission_factor` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `environmental_goal`
--
CREATE TABLE `environmental_goal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `department_id` int NOT NULL,
  `metric_type` varchar(100) NOT NULL,
  `target_value` decimal(12,2) NOT NULL,
  `current_value` decimal(12,2) DEFAULT '0.00',
  `deadline` date DEFAULT NULL,
  `status` enum('Active','Achieved','Missed','Cancelled') DEFAULT 'Active',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_goal_department` (`department_id`),
  CONSTRAINT `fk_goal_department` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `esg_policy`
--
CREATE TABLE `esg_policy` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` text,
  `document_url` varchar(500) DEFAULT NULL,
  `version` varchar(20) DEFAULT NULL,
  `status` enum('Draft','Active','Archived') DEFAULT 'Draft',
  `effective_date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `badges`
--
CREATE TABLE `badges` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text,
  `unlock_rule` json DEFAULT NULL,
  `icon_url` varchar(500) DEFAULT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `rewards`
--
CREATE TABLE `rewards` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `description` text,
  `points_required` int NOT NULL,
  `stock` int DEFAULT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ============================================================
-- JUNCTION TABLES
-- ============================================================

--
-- Table structure for table `employee_badges`
--
CREATE TABLE `employee_badges` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `badge_id` int NOT NULL,
  `awarded_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_employee_badge` (`employee_id`,`badge_id`),
  KEY `fk_eb_badge` (`badge_id`),
  CONSTRAINT `fk_eb_badge` FOREIGN KEY (`badge_id`) REFERENCES `badges` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_eb_employee` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `reward_redemptions`
--
CREATE TABLE `reward_redemptions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `reward_id` int NOT NULL,
  `points_spent` int NOT NULL,
  `redeemed_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('Pending','Fulfilled','Cancelled') DEFAULT 'Pending',
  PRIMARY KEY (`id`),
  KEY `fk_rr_employee` (`employee_id`),
  KEY `fk_rr_reward` (`reward_id`),
  CONSTRAINT `fk_rr_employee` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_rr_reward` FOREIGN KEY (`reward_id`) REFERENCES `rewards` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ============================================================
-- TRANSACTIONAL DATA (high write frequency)
-- ============================================================

--
-- Table structure for table `csr_activity`
--
CREATE TABLE `csr_activity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `category_id` int NOT NULL,
  `department_id` int NOT NULL,
  `description` text,
  `date` date DEFAULT NULL,
  `status` enum('Draft','Active','Completed','Cancelled') DEFAULT 'Draft',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_csr_category` (`category_id`),
  KEY `fk_csr_department` (`department_id`),
  CONSTRAINT `fk_csr_category` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_csr_department` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `employee_participation`
--
CREATE TABLE `employee_participation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `activity_id` int NOT NULL,
  `proof_url` varchar(500) DEFAULT NULL,
  `approval_status` enum('Pending','Approved','Rejected') DEFAULT 'Pending',
  `points_earned` int DEFAULT '0',
  `completion_date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_ep_employee` (`employee_id`),
  KEY `fk_ep_activity` (`activity_id`),
  CONSTRAINT `fk_ep_activity` FOREIGN KEY (`activity_id`) REFERENCES `csr_activity` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_ep_employee` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `challenge`
--
CREATE TABLE `challenge` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `category_id` int NOT NULL,
  `description` text,
  `xp` int NOT NULL DEFAULT '0',
  `difficulty` enum('Easy','Medium','Hard') DEFAULT 'Easy',
  `evidence_required` tinyint(1) DEFAULT '0',
  `deadline` date DEFAULT NULL,
  `status` enum('Draft','Active','Under Review','Completed','Archived') DEFAULT 'Draft',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_challenge_category` (`category_id`),
  CONSTRAINT `fk_challenge_category` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `challenge_participation`
--
CREATE TABLE `challenge_participation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `challenge_id` int NOT NULL,
  `employee_id` int NOT NULL,
  `progress` int DEFAULT '0',
  `proof_url` varchar(500) DEFAULT NULL,
  `approval_status` enum('Pending','Approved','Rejected') DEFAULT 'Pending',
  `xp_awarded` int DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_cp_challenge` (`challenge_id`),
  KEY `fk_cp_employee` (`employee_id`),
  CONSTRAINT `fk_cp_challenge` FOREIGN KEY (`challenge_id`) REFERENCES `challenge` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_cp_employee` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `policy_acknowledgement`
--
CREATE TABLE `policy_acknowledgement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `policy_id` int NOT NULL,
  `employee_id` int NOT NULL,
  `acknowledged_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('Pending','Acknowledged') DEFAULT 'Pending',
  PRIMARY KEY (`id`),
  KEY `fk_pa_policy` (`policy_id`),
  KEY `fk_pa_employee` (`employee_id`),
  CONSTRAINT `fk_pa_employee` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_pa_policy` FOREIGN KEY (`policy_id`) REFERENCES `esg_policy` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `audit`
--
CREATE TABLE `audit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `department_id` int NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text,
  `auditor` varchar(150) DEFAULT NULL,
  `status` enum('Scheduled','In Progress','Completed','Cancelled') DEFAULT 'Scheduled',
  `date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_audit_department` (`department_id`),
  CONSTRAINT `fk_audit_department` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `compliance_issue`
--
CREATE TABLE `compliance_issue` (
  `id` int NOT NULL AUTO_INCREMENT,
  `audit_id` int DEFAULT NULL,
  `department_id` int NOT NULL,
  `severity` enum('Low','Medium','High','Critical') DEFAULT 'Low',
  `description` text,
  `owner_employee_id` int DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `status` enum('Open','Resolved','Overdue') DEFAULT 'Open',
  `raised_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_ci_audit` (`audit_id`),
  KEY `fk_ci_department` (`department_id`),
  KEY `fk_ci_owner` (`owner_employee_id`),
  CONSTRAINT `fk_ci_audit` FOREIGN KEY (`audit_id`) REFERENCES `audit` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_ci_department` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_ci_owner` FOREIGN KEY (`owner_employee_id`) REFERENCES `employees` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `department_score`
--
CREATE TABLE `department_score` (
  `id` int NOT NULL AUTO_INCREMENT,
  `department_id` int NOT NULL,
  `environmental_score` decimal(5,2) DEFAULT '0.00',
  `social_score` decimal(5,2) DEFAULT '0.00',
  `governance_score` decimal(5,2) DEFAULT '0.00',
  `total_score` decimal(5,2) DEFAULT '0.00',
  `period` varchar(20) DEFAULT NULL,
  `calculated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_ds_department` (`department_id`),
  CONSTRAINT `fk_ds_department` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;