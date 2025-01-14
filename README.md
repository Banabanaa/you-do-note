
# You-Do-Note

**You-Do-Note** is a Django-based application for managing notes and to-do lists. It allows users to efficiently organize tasks, take notes, and streamline their productivity in a user-friendly interface.

## Features

- **User Authentication**
  - User login and signup functionality.
- **Notes Management**
  - Create, edit, delete, and copy notes.
- **To-Do List**
  - Add tasks, mark tasks as complete, and delete tasks.
- **Responsive Design**
  - Custom CSS for an intuitive user interface.
  
## Installation

### Prerequisites
- Python 3.x
- Django 3.x or higher
- SQLite (bundled with Python)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/you-do-note.git
   cd you-do-note
   ```

2. Install the required dependencies:
   ```bash
   pip install django
   ```

3. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application in your browser at:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. **Sign Up**  
   Create an account via the signup page.

2. **Log In**  
   Use your credentials to log in.

3. **Add Notes and Tasks**  
   Navigate to the homepage to manage notes and tasks.

4. **Edit/Delete**  
   Modify or delete existing notes and tasks directly from the homepage.

## License

This project is licensed under the MIT License.
