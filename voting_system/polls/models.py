from django.db import models

# Create your models here.

class Question(models.Model):

	question = models.CharField(max_length=200)
	public_date = models.DateTimeField('Date published')

	def __str__(self):
		return '{} {}'.format(self.question, self.public_date)

class Choice(models.Model):

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return '{} {}'.format(self.question.question, self.choice, self.votes)

