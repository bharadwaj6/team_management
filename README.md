# Team management

- Change database settings in settings.local.py

- `python manage.py migrate --settings=team_management.settings.local` to setup database in local.
- `python manage.py runserver_plus --settings=team_management.settings.local` to get Werkzeug server running in local.


- `/members/` endpoint
	* GET => list of all members
	* POST => create new members


- `/members/1/` endpoint
	* GET => show details of a member
	* POST => update all details of a member
	* PATCH => partial update for details of a member
	* DELETE => delete a member
