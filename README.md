Social Media Dashboard
This project implements a Social Media Dashboard using Flask for the backend and a frontend UI built with HTML, Tailwind CSS, and JavaScript. The dashboard fetches recent tweets and Instagram posts from specified usernames using Tweepy (for Twitter) and Instaloader (for Instagram).

## Features
- Backend (Flask)
Routes for fetching recent tweets (/api/twitter) and Instagram posts (/api/instagram).
Integration with Tweepy and Instaloader for data retrieval.
Frontend (HTML, Tailwind CSS, JavaScript)
Single-page application (index.html) displaying recent tweets and Instagram posts.
Dynamic fetching of data from the Flask backend using Axios.
## Dependencies
- Python 3.x
- Flask
= Tweepy
- Instaloader
- Axios (for frontend HTTP requests)

## Installation
Clone the repository:

```bash
git clone https://github.com/SHIV000000/resolve.ai-project-2-socialmedia-dashboard.git
```
```bash
cd resolve.ai-project-2-socialmedia-dashboard
```
## Install Python dependencies:

```bash
pip install flask tweepy instaloader
```
Start the Flask application:

```bash
python app.py
```
## Open your web browser and navigate to http://localhost:5000 to view the Social Media Dashboard.

## Acknowledgments
Completed with the help of resolve Ai for Round 2 of  Fullstack Engineering Resolv AI.
