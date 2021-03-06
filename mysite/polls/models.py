import datetime
from django.db import models
from django.utils import timezone

'''
models of question provides question text, publish date and end date
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('expiration date', default=None, null=True)

    def was_published_recently(self):
        '''
        to check that it was really published recently
        '''
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def is_published(self):
        '''
        to check that it is published
        '''
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        '''
        to check that this time you can vote
        '''
        now = timezone.now()
        return self.pub_date <= now < self.end_date

    def __str__(self):
        return self.question_text

'''
models of choice provides question, choice text and votes
'''
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
