from django.db import models

# Create your models here.
class NotesDB(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	todo = models.CharField(max_length=200)
	notes = models.CharField(max_length=500)

	def __str__(self):
		return str(self.date) + ' | ' + str(self.todo) + ' | ' + str(self.notes)
