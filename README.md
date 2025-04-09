# Fintech Payment API

A hybrid fintech application with a Node.js microservice for payment processing and a Django admin backend for transaction management and reporting.

## Overview

This project demonstrates a full-stack fintech application with two main components:
- **Node.js Microservice**: Handles payment processing, user authentication, and transaction creation using TypeORM and PostgreSQL.
- **Django Admin Backend**: Provides a secure admin interface for managing users and transactions, with advanced features like analytics, audit trails, and role-based access control.

The application uses a shared PostgreSQL database (`fintech_db`) to store user and transaction data, ensuring seamless integration between the two components.

## Features

### Node.js Microservice
- User registration and authentication with JWT.
- Payment processing API (`/api/payments/process`) to create transactions.
- PostgreSQL database integration with TypeORM.

### Django Admin Backend
- **Admin Interface**: Manage users and transactions with a user-friendly interface at `/admin/`.
- **Transaction Analytics Dashboard**: View total transactions, total amount, transactions by status, and a line chart of transactions over time using `pandas` and `django-chartjs`.
- **Role-Based Access Control (RBAC)**: Restrict admin access based on user roles (e.g., Managers can view, Auditors can edit).
- **Audit Trail**: Log all transaction changes (updates, deletes) with user details and timestamps.
- **Secure REST API**: Expose transaction data via `/api/transactions/` with token authentication and rate limiting.
- **Export Functionality**: Export transactions to CSV for reporting using `django-import-export`.

## Tech Stack
- **Backend (Microservice)**: Node.js, Express, TypeORM, PostgreSQL
- **Backend (Admin)**: Django, Django REST Framework, PostgreSQL
- **Database**: PostgreSQL (`fintech_db`)
- **Libraries**:
  - `pandas`, `django-chartjs` (analytics)
  - `django-ratelimit` (API rate limiting)
  - `django-import-export` (export functionality)

