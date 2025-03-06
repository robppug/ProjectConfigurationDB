# Project Configuration Manager

## Overview

Project Configuration Manager is a web-based application built using Flask and SQLAlchemy for managing project configurations. It allows users to add, edit, and delete project configurations, tracking cognitive and visual recognition features, compliance standards, and hardware platform compatibility.

## Features

- **Project Management:** Add, edit, and delete project configurations.
- **Cognitive & Visual Recognition Features:** Manage various AI-powered features such as inattentiveness detection, drowsiness monitoring, and object recognition.
- **Compliance Tracking:** Maintain compliance levels for ASPICE, ISO 26262, NCAP, and other industry standards.
- **Hardware & Platform Support:** Track platform compatibility across multiple hardware architectures.
- **User Interface:** Bootstrap-based responsive UI for managing configurations.

## Technologies Used

- Python (Flask)
- SQLAlchemy (SQLite database)
- HTML, CSS (Bootstrap 5)
- JavaScript (Bootstrap Scripts)

## Installation

### Prerequisites

Ensure you have Python installed (>=3.8) and a virtual environment set up.

### Setup Steps

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   flask db upgrade
   ```
5. Run the application:
   ```bash
   flask run
   ```

## Usage

- Open a browser and navigate to `http://127.0.0.1:5000/`.
- Use the interface to manage project configurations.

## File Structure

```
project_root/
│── static/                    # Static assets (CSS, images)
│──── styles.css               # CSS styles
│── templates/                 # HTML templates
│──── settings.html            # Settings page
│──── add.html                 # Add project page
│──── index.html               # Project list page
│──── _options.html            # Feature options macros
│──── _macros.html             # UI macros
│──── _messages.html           # Flash messages
│── app.py                     # Main Flask application
│── project_configurations.db  # SQLite database
│── requirements.txt           # Dependencies
│── ProjectConfigurationDB.sln # Visual Studio Solution (optional)
```

## Future Enhancements

- **User Authentication:** Add login/logout functionality.
- **Export Options:** Allow exporting project configurations to 1-pager or JSON (for engine configuration).

## License

This project is licensed under the MIT License.

## Author

Roberto Pugliese

