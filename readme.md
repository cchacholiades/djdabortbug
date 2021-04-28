# Steps to reproduce

------

1. `cd djdabortbug`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`
7. On a new terminal window `python manage.py rundramatiq`
8. Navigate to localhost:8000/admin
9. Under TestModels app add a new record, hit save & continue editing.
10. hit save once again on the newly created record, each time you hit save a scheduled job is being created
11. Go to Dramatiq tasks admin, you'll see the scheduled jobs. These are scheduled to be executed 271000 ms from the time you hit save.
12. The first job should be skipped, the second should execute => currently both execute.