# Blood Management System

## Overview
The **Blood Management System** is a web-based application developed using **Flask (Python)** and **MySQL**.  
It helps connect **blood donors, hospitals, and patients** by providing an easy platform to register donors, request blood, and search for available donors based on **blood group and location**.

The system aims to simplify the process of finding blood donors during emergencies and improve blood request management.

---

## Features

- **Donor Registration**
  - Donors can register with personal details, blood group, and location.

- **Hospital Blood Requests**
  - Hospitals can submit blood requests for specific blood groups.

- **Search Donors**
  - Users can search donors based on **blood type and location**.

- **Request Management**
  - Efficient handling and tracking of blood requests.

- **Filtering Options**
  - Filters to quickly find suitable donors.

- **Responsive User Interface**
  - Accessible through any browser with a user-friendly interface.

---

## Technologies Used

| Technology | Description |
|-----------|-------------|
| Python | Backend programming |
| Flask | Web framework |
| MySQL | Database management |
| HTML | Web page structure |
| CSS | Styling |
 | Client-side functionality |

---

## System Architecture

```
User Interface (HTML/CSS)
        |
        v
Flask Web Application (Python Backend)
        |
        v
MySQL Database
```

---

## Database Structure

### Donor Table
- donor_id
- name
- blood_group
- contact_number
- location

### Blood Request Table

- hospital_name
- blood_group
- location
- request_date
- status

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VarshithJ07/blood-management-system.git
cd blood-management-system
```

### 2. Install Required Packages

```bash
pip install flask
pip install mysql-connector-python
```

### 3. Setup Database

Create a MySQL database:

```sql
CREATE DATABASE blood_management;
```

Import the database schema if available.

---

### 4. Run the Application

```bash
python app.py
```

Open the application in your browser:

```
http://127.0.0.1:5000
```





---

## Future Enhancements

- Email or SMS notifications for blood requests  
- User authentication and login system  
- Integration with hospital databases  
- Mobile application support  
- Real-time donor availability tracking  

---

## Use Cases

This system can be used by:

- Hospitals
- Blood banks
- Emergency response teams
- Community blood donation programs

---

