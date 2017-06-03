# Team management

- Change database settings in settings.py


- `python manage.py migrate` to setup database


- `/members/` endpoint
	* GET => list of all members
	* POST => create new members


- `/members/1/` endpoint
	* GET => show details of a member
	* POST => update all details of a member
	* PATCH => partial update for details of a member
	* DELETE => delete a member
