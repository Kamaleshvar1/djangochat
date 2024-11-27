# Django Project with Channels and Redis

This is a Django web application that uses **Django Channels** and **Redis** to enable real-time features like WebSockets. This project is a basic setup that demonstrates how to integrate Django Channels with Redis as the channel layer backend. 

## Features
- Real-time updates using WebSockets
- Django Channels setup for asynchronous functionality
- Redis for managing connections and messaging
- Supports Django 4.x and Python 3.12+

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12** (or later)
- **Django 4.x**
- **Redis** (for Channels' backend)

## Setting up the Project Locally

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

Start by cloning the repository to your local system:

git clone https://github.com/Kamaleshvar1/djangochat.git
cd djangochat

### 2. Create a Virtual Environment
Create a virtual environment to manage dependencies:

python -m venv .venv
Activate the virtual environment:

On Windows:
.venv\Scripts\activate

On macOS/Linux:
source .venv/bin/activate

### 3. Install Dependencies

Install the required packages:

pip install -r requirements.txt

### 4. Install and Run Redis
You need Redis to act as a channel layer for Django Channels.

Option 1: Running Redis via Docker
If you have Docker installed, you can run Redis in a container:
docker run -d --name redis-server -p 6379:6379 redis

Option 2: Running Redis on WSL (Windows only)
Enable WSL (Windows Subsystem for Linux) and install a Linux distro like Ubuntu.

Install Redis on Ubuntu:
sudo apt update
sudo apt install redis-server
sudo service redis-server start

Option 3: Running Redis on macOS/Linux
You can install Redis using the package manager (e.g., brew install redis on macOS) or by downloading and running Redis natively.

### 5. Apply Migrations
Run Django migrations to set up your database:
python manage.py migrate

### 6. Run the Development Server
Start the Django development server:
python manage.py runserver

Your project should now be running at http://127.0.0.1:8000/.


