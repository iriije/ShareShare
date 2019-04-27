from django.db import models
from django.utils import timezone
from member.models import User
from item.models import Item

   
class Rent(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    sharee = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    reserationTime = models.DateTimeField(auto_now_add=True)
    rentDate = models.DateField()
    rentTime = models.TimeField()
    dueDate = models.DateField()
    dueTime = models.TimeField()
    extensionTime = models.DateTimeField(null=True)

    ONE = '1'
    ONE_HALF = '1.5'
    TWO = '2'
    TWO_HALF = '2.5'
    THREE = '3'
    THREE_HALF = '3.5'
    FOUR = '4'
    FOUR_HALF = '4.5'
    FIVE = '5'
    
    STAR_CHOICES = (
        (ONE, '1'),
        (ONE_HALF, '1.5'),
        (TWO, '2'),
        (TWO_HALF, '2.5'),
        (THREE, '3'),
        (THREE_HALF, '3.5'),
        (FOUR, '4'),
        (FOUR_HALF, '4.5'),
        (FIVE, '5')
    )

    star = models.CharField(max_length=10, choices = STAR_CHOICES, default=THREE)

    review = models.TextField()
    returnTime = models.DateTimeField(null=True)

    WORST = 'worst'
    BAD = 'bad'
    NORMAL = 'normal'
    GOOD = 'good'
    BEST = 'best'
    
    RETURN_STATUS_CHOICES = (
        (WORST, 'worst'),
        (BAD, 'bad'),
        (NORMAL, 'normal'),
        (GOOD, 'good'),
        (BEST, 'best')
    )

    returnStatus = models.CharField(max_length=10, choices = RETURN_STATUS_CHOICES, default=GOOD)

    objects = models.Manager()