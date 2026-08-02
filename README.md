# Retail Analytics Data Platform

A production-inspired Data Engineering project that builds a complete ETL pipeline for an e-commerce retail dataset.

The objective of this project is not simply to load CSV files into MySQL, but to design an extensible, maintainable, and production-style ingestion framework that follows industry engineering practices.

This project serves as the foundation for a complete Retail Analytics Data Platform that will later evolve into a dimensional data warehouse, analytical dashboards, workflow orchestration, and cloud deployment.

---

# Project Objectives

- Design a normalized OLTP database.
- Build a reusable ETL ingestion framework.
- Validate incoming datasets before loading.
- Maintain transactional integrity.
- Implement structured logging.
- Handle failures gracefully.
- Build reusable components instead of writing dataset-specific code.
- Prepare the foundation for a Data Warehouse.

---

# Dataset

The project uses the Brazilian E-Commerce Public Dataset (Olist).

Datasets included:

- Customers
- Orders
- Order Items
- Payments
- Reviews
- Products
- Sellers
- Product Category Translation
- Geolocation

---

# Tech Stack

Python

- Pandas
- mysql-connector-python
- python-dotenv
- Logging

Database

- MySQL

Tools

- VS Code
- Git
- GitHub

---

# Project Architecture

```
CSV Files
     │
     ▼
Loader
     │
     ▼
Validator
     │
     ▼
Transformer
     │
     ▼
Loader
     │
     ▼
MySQL (OLTP)
     │
     ▼
Data Warehouse (Future)
```

---

# Project Structure

```
Retail-Analytics-Data-Platform/

│
├── Data/
│
├── loader.py
├── validator.py
├── transform.py
├── load.py
├── database.py
├── main.py
│
├── .env
├── requirements.txt
├── pipeline.log
│
└── README.md
```

---

# Database Design

The relational database was designed manually before any coding began.

The design includes:

- Primary Keys
- Foreign Keys
- Relationship Analysis
- Normalization
- Composite Keys
- Referential Integrity

Tables

- customers
- orders
- order_items
- order_payments
- products
- sellers
- reviews
- geolocation
- product_category_name_translation

---

# ETL Workflow

## 1. Extract

- Read CSV files
- Convert into Pandas DataFrames

---

## 2. Validate

Validation includes:

- Required column validation
- Empty dataset detection
- Primary key NULL validation
- Duplicate primary key validation
- Configuration-driven validation

Future validations:

- Data type validation
- Business rule validation
- Foreign key validation
- Value range validation

---

## 3. Transform

Current

- Preparing datasets for loading

Future

- Data cleaning
- Data standardization
- Derived columns
- Feature engineering

---

## 4. Load

- Batch inserts using executemany()
- Database transactions
- Rollback support
- Connection management

---

# Logging

The pipeline records:

- Pipeline execution
- Validation failures
- Database errors
- Successful loads

Logs are stored in

```
pipeline.log
```

---

# Error Handling

The pipeline follows fail-fast principles.

Critical failures immediately stop processing.

Examples

- Missing columns
- Duplicate primary keys
- NULL primary keys
- Database failures

---

# Design Principles

The project follows software engineering best practices.

- Separation of Concerns
- Configuration-driven Validation
- Modular Design
- Reusable Components
- Transaction Management
- Scalable Architecture

---

# Current Progress

Completed

- Database Schema Design
- OLTP Database
- Generic Validator
- Database Connectivity
- Transaction Management
- Batch Loading
- Logging Framework

In Progress

- Generic Loader
- Generic ETL Framework

Upcoming

- Data Warehouse
- Star Schema
- Fact Tables
- Dimension Tables
- Incremental Loading
- Airflow
- Docker
- Cloud Deployment
- BI Dashboards

---

# Future Enhancements

- Apache Airflow
- Docker
- AWS
- Azure
- Snowflake
- dbt
- Data Quality Monitoring
- CI/CD Pipeline
- Unit Testing
- Data Warehouse Automation

---

# Learning Outcomes

This project demonstrates practical experience with

- Data Engineering
- ETL Design
- Relational Database Design
- SQL
- Python
- Pandas
- MySQL
- Transactions
- Logging
- Software Architecture
- Production-style Development

---

# Disclaimer

This project is built for educational purposes while following production-inspired engineering practices. The goal is to simulate how data ingestion pipelines are designed, validated, and maintained in real-world environments.