# Pocket Planner Documentation

## Overview
Pocket Planner is a personal finance management application built with Django. It allows users to track their transactions, categorize expenses and incomes, convert currencies, and visualize financial data through interactive charts.

---

## Table of Contents
1. [Project Structure](#project-structure)
2. [Features](#features)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [API Integration](#api-integration)
6. [Database Schema](#database-schema)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Structure
The project is organized into the following main apps:
- **`users`**: Handles user authentication, profiles, and base currency settings.
- **`transactions`**: Manages financial transactions (income/expenses) with CRUD functionality.
- **`categories`**: Allows users to create and manage categories for transactions.
- **`currencies`**: Provides currency conversion and rate updates using an external API.

---

## Features
### User Management
- **Signup/Login/Logout**: Users can create accounts, log in, and manage their profiles.
- **Profile Management**: Users can update their details, including their base currency.
- **Account Deletion**: Users can delete their accounts.

### Transactions
- **CRUD Operations**: Create, read, update, and delete transactions.
- **Categories**: Assign transactions to user-defined categories.
- **Currency Conversion**: Automatically converts transaction amounts to the user's base currency.

### Categories
- **Create/Edit/Delete**: Users can manage categories for better organization of transactions.
- **Category Statistics**: View detailed statistics and charts for each category.

### Currencies
- **Currency List**: View all available currencies with their exchange rates.
- **Currency Converter**: Convert amounts between different currencies.
- **Rate Updates**: Admins can update currency rates via an external API.

### Visualizations
- **Charts**: Interactive pie charts display income and expenses by category.

---

## Installation and Setup

### Prerequisites
- Python 3.9+
- PostgreSQL
- Dependencies listed in `requirements.txt`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/tu-usuario/pocket-planner.git
   cd pocket-planner
   ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure environment variables:
    ```bash
    SECRET_KEY=your_secret_key
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_HOST=localhost
    DB_PORT=5432
    EXCHANGERATE_API_KEY=your_api_key
    ```
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

---

## Usage

### URLs
| URL                        | Method | Description                                   |
|----------------------------|--------|-----------------------------------------------|
| `/`                        | GET    | Home page with app information.              |
| `/users/signup/`           | POST   | Create a new user account.                   |
| `/users/login/`            | POST   | Log in to an existing account.               |
| `/users/logout/`           | POST   | Log out of the current session.              |
| `/users/profile/`          | GET    | View user profile details.                   |
| `/users/update/`           | POST   | Update user profile information.             |
| `/users/delete/`           | POST   | Delete the user account.                     |
| `/transactions/`           | GET    | List all transactions for the user.          |
| `/transactions/create/`    | POST   | Create a new transaction.                    |
| `/transactions/<id>/edit/` | POST   | Edit an existing transaction.                |
| `/transactions/<id>/delete/`| DELETE| Delete a specific transaction.              |
| `/categories/`             | GET    | List all categories created by the user.     |
| `/categories/create/`      | POST   | Create a new category.                       |
| `/categories/<id>/edit/`   | POST   | Edit a category name.                        |
| `/categories/<id>/delete/` | POST   | Delete a specific category.                  |
| `/currencies/`             | GET    | List all available currencies.               |
| `/currencies/converter/`   | POST   | Convert amounts between two currencies.      |
| `/currencies/update/`      | PUT    | Update currency rates (admin only).          |

---

## API Integration
Pocket Planner uses the [ExchangeRate-API](https://www.exchangerate-api.com/) to fetch and update currency exchange rates. To use this feature, you need an API key, which should be configured in the `.env` file.

---

## Database Schema
### User
| Field          | Type         | Description                     |
|----------------|--------------|---------------------------------|
| id             | Primary Key  | Unique identifier for the user.|
| username       | CharField    | Username of the user.          |
| first_name     | CharField    | First name of the user.        |
| last_name      | CharField    | Last name of the user.         |
| password       | CharField    | Hashed password.               |
| base_currency  | ForeignKey   | User's base currency.          |

### Transaction
| Field            | Type         | Description                     |
|------------------|--------------|---------------------------------|
| id               | Primary Key  | Unique identifier for the transaction.|
| amount           | FloatField   | Transaction amount.            |
| type_transaction | CharField    | "Deposit" or "Withdrawal".      |
| date             | DateTimeField| Timestamp of the transaction.  |
| user             | ForeignKey   | User who owns the transaction. |
| category         | ForeignKey   | Category of the transaction.   |
| currency         | ForeignKey   | Currency of the transaction.   |

### Category
| Field  | Type         | Description                     |
|--------|--------------|---------------------------------|
| id     | Primary Key  | Unique identifier for the category.|
| name   | CharField    | Name of the category.          |
| user   | ForeignKey   | User who owns the category.    |

### Currency
| Field      | Type         | Description                     |
|------------|--------------|---------------------------------|
| id         | Primary Key  | Unique identifier for the currency.|
| code       | CharField    | Currency code (e.g., USD, EUR).|
| name       | CharField    | Full name of the currency.     |
| rate_to_usd| FloatField   | Exchange rate to USD.          |
| updated_at | DateTimeField| Last update timestamp.         |

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m "Add your feature description"`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.
