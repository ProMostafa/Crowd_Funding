from django.db import models
from account.models import MyUser
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length=70)
    details = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_target = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    tags = TaggableManager()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # for get this tags from template as strings
    def get_tags(self):
        tags = ""
        for tag in self.tags.all():
            tags += f'{tag},'
        return tags

    def get_absolute_url(self):
        return reverse('home')

    # calc number of rating for project
    def number_of_rating(self):
        # rating = Rate.objects.filter(project=self)
        return Rate.objects.filter(project=self).count()

    # calc average rating
    def average_rating(self):
        sum = 0
        rating = Rate.objects.filter(project=self)
        for rate in rating:
            sum += rate.rating
        if len(rating):
            return sum / len(rating)
        return 0

    def donation_collect(self):
        sum = 0
        donations = Denote.objects.filter(project=self)
        for donation in donations:
            sum += donation.amount
        return sum

    class Meta:
        constraints = [
            models.CheckConstraint(name='end_date_after_start_date',
                                   check=models.Q(end_date__gt=models.F('start_date')))
        ]

    def __str__(self):
        return self.title


class ProjectPicture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Denote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_photo(self):
        if ProjectPicture.objects.filter(project=self.project):
            return ProjectPicture.objects.filter(project=self.project).first().image
        return False


class Rate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    # for unique (user and project) 
    class Meta:
        unique_together = (('user', 'project'),)
        index_together = (('user', 'project'),)


class ProjectReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class CommentReport(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

# class UserProfile(models.Model):
#     user  = models.OneToOneField(User)
#     avatar= models.ImageField()
