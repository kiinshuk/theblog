# TheBlog - A Modern Django Blogging Platform

![Django Version](https://img.shields.io/badge/Django-5.2.6-green.svg)
![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A feature-rich, modern blogging platform built with Django. TheBlog offers a clean, intuitive interface for writers to share their stories and for readers to discover engaging content.

**Live Demo:** [https://kiinshuk.pythonanywhere.com/](https://kiinshuk.pythonanywhere.com/)

---

## 📋 Table of Contents
1. [Features](#-features)
2. [Quick Start](#-quick-start)
3. [Project Structure](#-project-structure)
4. [Database Models](#-database-models)
5. [Usage Guide](#-usage-guide)
6. [Deployment](#-deployment)
7. [Configuration](#-configuration)
8. [Testing](#-testing)
9. [Troubleshooting](#-troubleshooting)
10. [Contributing](#-contributing)
11. [License & Contact](#-license--contact)

---

## ✨ Features

### 📝 Content Management
- **Create, Edit, Delete Posts** - Full CRUD operations for blog posts
- **Rich Text Editor** - Write posts with formatting using Summernote
- **Post Categories** - Organize content with categories
- **Post Snippets** - Custom preview text for posts
- **Header Images** - Add featured images to posts

### 👤 User Features
- **User Authentication** - Register, login, and profile management
- **User Profiles** - Customizable profiles with bio and social links
- **Profile Pictures** - Upload custom avatars
- **Author Pages** - Dedicated pages showing all posts by an author

### 💬 Engagement
- **Like System** - Users can appreciate posts
- **Comments** - Engage with content through comments
- **Post Categories** - Browse content by topic
- **Pagination** - Smooth navigation through posts

### 🎨 Design
- **Responsive Design** - Works perfectly on all devices
- **Modern UI** - Clean, professional interface
- **Bootstrap 5** - Latest Bootstrap framework
- **Custom CSS** - Enhanced styling with animations
- **Dark Mode Support** - Automatic dark theme based on system preferences

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/theblog.git
cd theblog

# 2. Create and activate virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo "SECRET_KEY=your-secret-key-here" > .env
echo "DEBUG=True" >> .env
echo "DATABASE_URL=sqlite:///db.sqlite3" >> .env

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver

# 8. Access the application
# Main site: http://127.0.0.1:8000/
# Admin panel: http://127.0.0.1:8000/admin/
