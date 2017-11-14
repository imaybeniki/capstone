from django.contrib.auth.models import User

user = User.objects.create_user('TiMazing', 'timothysmay@gmail.com', 'capstone123')

user.first_name = 'Tim'
user.last_name = 'May'

user.save()