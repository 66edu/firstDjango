from django.db import models


class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.question
	
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length = 200)
	votes = models.IntegerField(default=0)

	
	def __str__(self):
		return self.choice


















