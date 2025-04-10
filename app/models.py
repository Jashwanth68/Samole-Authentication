from djongo import models  # or use mongoengine if you're using that

class FirebaseUser(models.Model):
    uid = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    picture = models.URLField(blank=True, null=True)
    provider = models.CharField(max_length=64, default='google')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
