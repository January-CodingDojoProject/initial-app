from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create and validate User model.
class UserManager(models.Manager):
	def validate(self, form_data):
		errors = []

		if len(form_data['first_name']) < 2:
			errors.append("First name must be at least 2 characters long")
		if len(form_data['last_name']) < 2:
			errors.append("Last name must be at least 2 characters long")
		if len(form_data['username']) < 4:
			errors.append("Username must be at least 4 characters long")
		if not EMAIL_REGEX.match(form_data['email']):
			errors.append("Email must be valid")
		if len(form_data['password']) < 8:
			errors.append("Password must be at least 8 characters long")

		if self.filter(username=form_data['username']):
			errors.append("Username already in use")
		if self.filter(email=form_data['email']):
			errors.append("Email already in use")

		return errors

	def create_user(self, form_data):
		pw_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
		return self.create(
		first_name=form_data['first_name'],
		last_name=form_data['last_name'],
		email=form_data['email'],
		username=form_data['username'],
		pw_hash=pw_hash,
		)

	def check_login(self, form_data):
		errors = []
		try:
			user = self.get(username=form_data['username'])
		except:
			errors.append("Username or password invalid")
			return (False, errors)
		
		if bcrypt.checkpw(form_data['password'].encode(), user.pw_hash.encode()):
			return (True, user)
		else:
			errors.append("Username or password invalid")
			return (False, errors)
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pw_hash = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __str__(self):
		return self.email

# Create and validate Tour model.
class TourManager(models.Manager):
	def validate(self, form_data):
		errors = []

		if len(form_data['date']) > 5:
			errors.append("date must not exceed 5 characters")
		if len(form_data['city']) < 2:
			errors.append("city must be at least 2 characters long")
		if len(form_data['state']) > 2:
			errors.append("State must be 2 characters only")
		if len(form_data['venue']) < 8:
			errors.append("Venue must be at least 8 characters long")
		return errors

	def create_tour(self, form_data):
		manager = User.objects.get(id=form_data['manager'])
		return self.create(
		date=form_data['date'],
		city=form_data['city'],
		state=form_data['state'],
		venue=form_data['venue'],
		manager=manager,
		)
class Tour(models.Model):
	date = models.CharField(max_length=5)
	city = models.CharField(max_length=120)
	state = models.CharField(max_length=2)
	venue = models.CharField(max_length=250)
	manager = models.ForeignKey(User, related_name="tours")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = TourManager()

	def __str__(self):
		return self.venue

# Create and validate product model.
class Product(models.Model):
	name = models.CharField(max_length=120)
	price = models.IntegerField()
	quantity = models.IntegerField()

	def __str__(self):
		return self.name