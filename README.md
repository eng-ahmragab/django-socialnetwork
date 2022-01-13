# django-socialnetwork
a social network app built with django





# Features:
- User authentication and authorization: Signup, Login and Protected Pages.
- Add, edit and delete posts with picture uploads. Only post owners are authorized to modify/delete.
- Comment on posts
- Like on posts
- Share posts (still in progress ..)
- Edit personal profile
- Search for users, follow and unfollow.




![App Screenshot](https://i.ibb.co/xgm5Zrd/screenshot.png)



# Development Setup
1) On the root directory, create a file: .env
2) Add the needed environment variables
```bash
  SECRET_KEY=XXXX
  DEBUG=True
```
3) Setup a virtual environment:
```bash
  pip3 install virtualenv
  mkdir venv
  python3 -m virtualenv venv
```

4) Activate the virtual environment:
- On Linux and OSX
```bash
  source venv/bin/activate
```
- On Windows
```bash
  .\venv\Scripts\activate.bat
```

5) Install the dependencies:
```bash
  pip3 install -r requirements.txt
```

6) Migrate any pending db changes:
```bash
  python manage.py makemigrations
  python manage.py migrate
```

7) Run the development server
```bash
  python manage.py runserver
```

8) you can reach the web app at: http://localhost:8000

