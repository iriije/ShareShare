from django.db import models
from django.utils import timezone



class Sharer(models.Model):
    userMail = models.CharField(max_length=100)

class ItemType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Items(models.Model):
    itemId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, help_text='공유하고 싶은 item의 이름을 입력해주세요.')
    itemType = models.ManyToManyField(ItemType)
    photo = models.ImageField()
    userMail = models.ForeignKey(Sharer,on_delete=models.DO_NOTHING)
    deposit = models.IntegerField()
    rentalFeePerHour = models.IntegerField()
    
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




class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
