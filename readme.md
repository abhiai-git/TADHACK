# TADHACK Project - IIT Chicago MSCDOR I

This project was developed for the TADHACK hackathon during my time at IIT Chicago, MSCDOR I, where it received an outstanding presentation award.

## Overview

The TADHACK project is a Flask-based web application that integrates with various communication APIs, including Vidyo.io for video conferencing tokens, Phaxio for faxing, and Telnyx for SMS messaging. The application provides user authentication and different roles (admin/user).

## Features

- **User Authentication**: Secure login system with distinct roles for administrators and regular users.
- **Vidyo.io Integration**: Generates Vidyo.io tokens for video conferencing.
- **Phaxio Integration**: Sends faxes using the Phaxio API.
- **Telnyx SMS Integration**: Sends SMS messages via the Telnyx API.
- **Database**: Uses MongoDB for user management.

## Project Structure

- `app/`: Contains the core Flask application.
    - `__init__.py`: Initializes the Flask app and extensions.
    - `forms.py`: Defines web forms using Flask-WTF.
    - `user.py`: User model and login validation.
    - `views.py`: Defines the application routes and logic for handling requests, including API integrations.
    - `static/`: Static files (CSS, JavaScript, images).
    - `templates/`: HTML templates for rendering pages.
- `config.py`: Configuration settings for the application.
- `requirements.txt`: Lists all Python dependencies.
- `run-dev.py`: Script to run the development server.
- `generateToken.py`: Likely a script for generating tokens (e.g., Vidyo.io).
- `populateDB.py`: Script to populate the database with initial data.
- `userdata.csv`: CSV file for user data, possibly used by `populateDB.py`.
- `cert.pem`, `key.pem`: SSL certificates for secure communication.
- `Presentation.pptx`: The presentation file for the hackathon.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone [repository_url]
   cd TADHACK
   ```

2. **Install dependencies**:
   It is highly recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the application**:
   Update `config.py` with your MongoDB connection details and API keys for Phaxio and Telnyx.

4. **Populate the database (optional)**:
   If you have `populateDB.py` and `userdata.csv`, you can run:
   ```bash
   python populateDB.py
   ```

5. **Run the development server**:
   ```bash
   python run-dev.py
   ```
   The application will typically run on `http://127.0.0.1:9090`.

## Technologies Used

- **Flask**: Web framework
- **MongoDB**: NoSQL Database
- **Vidyo.io**: Video conferencing API
- **Phaxio**: Fax API
- **Telnyx**: SMS API
- **Flask-Login**: User session management
- **Flask-WTF**: Web forms
- **Requests**: HTTP library
- **Pandas/Numpy/Scipy**: Data analysis libraries (likely for some backend processing or analytics)

## Awards

- Outstanding Presentation Award at TADHACK, IIT Chicago MSCDOR I.
- **Presentation Video**: [YouTube Link](https://www.youtube.com/watch?v=eNrSCJW7r5Y)
- **TADHACK Chicago 2017 Winners**: [Winners Page](https://blog.tadhack.com/2017/09/26/tadhack-chicago-2017/)
