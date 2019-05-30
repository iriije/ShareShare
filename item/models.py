from django.db import models
from django.conf import settings
from django.utils import timezone
from member.models import User
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

class ItemType(models.Model):
    BOOK = 'B'
    CAMP = 'C'
    LIFE = 'L'
    WEAR = 'W'
    ELSE = 'E'

    CATEGORY_CHOICES = (
        (BOOK, '도서/서적'),
        (CAMP, '캠핑/레져'),
        (LIFE, '생활/가전'),
        (WEAR, '의류/패션'),
        (ELSE, '사물/잡화')
    )

    objects = models.Manager()

    name = models.CharField(max_length=10, choices = CATEGORY_CHOICES, default=ELSE)


    def __str__(self):
        return self.name


class Item(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20, help_text='공유하고 싶은 item의 이름을 입력해주세요.')
    itemType = models.ManyToManyField(ItemType)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    deposit = models.IntegerField()
    rentalFeePerHour = models.IntegerField()
    tag_set = models.ManyToManyField('Tag', blank=True)
    
    AVAILABLE = 'A'
    REPAIR = 'R'
    SHARED = 'S'
    BROKEN = 'B'
    
    STATUS_CHOICES = (
        (AVAILABLE,'이용 가능'),
        (REPAIR, '수리중'),
        (SHARED, '공유중'),
        (BROKEN,'고장')
    )

    currentStatus = models.CharField(max_length=10, choices = STATUS_CHOICES, default=AVAILABLE)

    DIRECT = 'D'
    SHIPPING = 'S'
    BOTH = 'B'

    SHIPPINGMETHOD_CHOICES = (
        (DIRECT, '직접 거래'),
        (SHIPPING, '택배'),
        (BOTH, '직접거래/택배')
    )
    
    
    shippingMethod = models.CharField(max_length=10,choices=SHIPPINGMETHOD_CHOICES, default = DIRECT)

    location = models.CharField(max_length=30)
    maxRentTime = models.IntegerField()
    explanation = models.TextField()
    uploadDate = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
