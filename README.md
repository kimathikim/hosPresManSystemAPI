# Hospital Prescription Management System (HPMS)

---

## Project Overview

The Hospital Prescription Management System (HPMS) is designed to manage and streamline the process of handling prescriptions between hospitals, pharmacies, and patients. The system ensures secure and efficient prescription management, enabling hospitals to create prescriptions and pharmacies to retrieve and dispense them. The system also allows for medication management by pharmacists.

## Features

- **User Management**: Handle different user roles including Hospital Staff, Pharmacy Staff, and Pharmacists.
- **Prescription Management**: Hospitals can create and manage prescriptions for patients.
- **Pharmacy Integration**: Pharmacies can retrieve and dispense prescriptions securely.
- **Medication Management**: Pharmacists can manage the inventory of medications.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Schema Validation**: Marshmallow
- **API Documentation**: Flasgger
- **Security**: bcrypt

## Prerequisites

- Python 3.10+
- MySQL

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/hosPresManSystemAPI.git
   cd hosPresManSystemAPI
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your MySQL database**:

   - Create a new database:
     ```sql
     CREATE DATABASE HPMS;
     ```

5. **Set up environment variables**:
   You can export the environment variables directly in your terminal or create a `.env` file.

   ```bash
   export HPMS_MYSQL_USER=root
   export HPMS_MYSQL_PWD=*****
   export HPMS_MYSQL_HOST=localhost
   export HPMS_MYSQL_DB=HPMS
   ```

   Or, add the following to a `.env` file in the root directory:

   ```bash
   HPMS_MYSQL_USER=root
   HPMS_MYSQL_PWD=*****
   HPMS_MYSQL_HOST=localhost
   HPMS_MYSQL_DB=HPMS
   ```

## Running the Application

To run the application in development mode, use the following command:

```bash
HPMS_MYSQL_USER=root HPMS_MYSQL_PWD=***** HPMS_MYSQL_HOST=localhost HPMS_MYSQL_DB=HPMS python3 -m run
```

The application will start, and you can access it via `http://localhost:5000`.

## API Documentation

The project uses Flasgger for API documentation. Once the application is running, you can access the API documentation at:

```
http://localhost:5000/apidocs
```

## Directory Structure

```
hosPresManSystemAPI/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── hospital.py
│   │   ├── pharmacy.py
│   │   ├── medication.py
│   │   ├── audit_log.py
│   │   └── engine/
│   │       ├── db_storage.py
│   │       └── ...
│   ├── factory.py
│   └── ...
├── requirements.txt
├── run.py
    ...
└── README.md
```

## Contributing

Contributions are welcome! Please create a pull request with a detailed explanation of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out to the project maintainer at `briankimathi94@gmail.com`.

---

Replace `*****` with your actual MySQL password, and update any placeholders with the correct information related to your project.
