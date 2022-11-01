from django.db import models
from django.core.files import File
from PIL import Image, ImageOps
from io import BytesIO
from core import validators

def Hosts_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Hosts_Cover_Images', str(instance.host_name) + "_" + str(filename)])

def Categories_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Categories_Cover_Images', str(instance.category_name) + "_" + str(filename)])

def Podcasts_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Podcasts_Cover_Images', str(instance.podcast_name) + "_" + str(filename)])
    
def Seasons_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Seasons_Cover_Images', str(instance.season_name) + "_" + str(filename)])

def Episode_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Episode_Cover_Images', str(instance.episode_name) + "_" + str(filename)])

def Episode_Files(instance, filename):
    return '/'.join(['Media_Files', 'Episode_Files', str(instance.season_id), str(instance.episode_name) + "_" + str(filename)])

class HostsModel(models.Model):

    class Meta:
        ordering = ['id']

    host_name = models.CharField(null=False, blank=True, max_length=256)
    host_title = models.CharField(null=True, blank=True, max_length=256)
    host_rating = models.IntegerField(null=True, blank=True, default=0)
    host_status = models.BooleanField(null=False, blank=True, default=False)
    host_description = models.CharField(null=True, blank=True, max_length=4096)
    host_viewcount = models.IntegerField(null=False, blank=True, default=0)
    host_profileImage = models.ImageField(null=False, blank=True, upload_to=Hosts_Cover_Images, validators=[validators.validate_image_extension], max_length=4092)
    host_FUI = models.CharField(null=False, blank=True, unique=True, max_length=1023)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        image = Image.open(self.host_profileImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.host_profileImage))
        self.host_profileImage = compressed_image
        super(HostsModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.host_name}"


class CategoriesModel(models.Model):

    class Meta:
        ordering = ['id']

    category_name = models.CharField(null=False, blank=True, max_length=256)
    category_rating = models.IntegerField(null=True, blank=True, default=0)
    category_status = models.BooleanField(null=False, blank=True, default=False)
    category_description = models.CharField(null=True, blank=True, max_length=4096)
    category_viewcount = models.IntegerField(null=False, blank=True, default=0)
    category_coverImage = models.ImageField(null=False, blank=True, upload_to=Categories_Cover_Images, validators=[validators.validate_image_extension], max_length=4092)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        image = Image.open(self.category_coverImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.category_coverImage))
        self.category_coverImage = compressed_image
        super(CategoriesModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.category_name}"

class PodcastsModel(models.Model):

    class Meta:
        ordering = ['id']

    podcast_name = models.CharField(null=False, blank=True, max_length=256)
    podcast_rating = models.IntegerField(null=True, blank=True, default=0)
    podcast_status = models.BooleanField(null=False, blank=True, default=False)
    podcast_description = models.CharField(null=True, blank=True, max_length=4096)
    podcast_viewcount = models.IntegerField(null=False, blank=True, default=0)
    podcast_coverImage = models.ImageField(null=False, blank=True, upload_to=Podcasts_Cover_Images, validators=[validators.validate_image_extension], max_length=4092)
    host = models.ForeignKey(HostsModel,related_name="podcast_host", null=False, blank=True, default=1, on_delete=models.DO_NOTHING)
    category= models.ForeignKey(CategoriesModel,related_name="podcast_category",null=False, blank=True, default=1, on_delete=models.DO_NOTHING)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        image = Image.open(self.podcast_coverImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.podcast_coverImage))
        self.podcast_coverImage = compressed_image
        super(PodcastsModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.podcast_name}"

class SeasonsModel(models.Model):

    class Meta:
        ordering = ['id']

    season_name = models.CharField(null=False, blank=True, max_length=256)
    season_rating = models.IntegerField(null=True, blank=True, default=0)
    season_status = models.BooleanField(null=False, blank=True, default=False)
    season_releaseDate = models.DateField(null=True, blank=True)
    season_description = models.CharField(null=True, blank=True, max_length=4096)
    season_viewcount = models.IntegerField(null=False, blank=True, default=0)
    season_coverImage = models.ImageField(null=False, blank=True, upload_to=Seasons_Cover_Images, validators=[validators.validate_image_extension], max_length=4092)
    season_price = models.IntegerField(null=False, blank=True, default=40)
    podcast = models.ForeignKey(PodcastsModel, related_name="season_podcast",null=False, blank=True, default=1, on_delete=models.DO_NOTHING)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        image = Image.open(self.season_coverImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.season_coverImage))
        self.season_coverImage = compressed_image
        super(SeasonsModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.season_name}"

class EpisodesModel(models.Model):

    class Meta:
        ordering = ['id']

    episode_name = models.CharField(null=False, blank=True, max_length=256)
    episode_rating = models.IntegerField(null=True, blank=True, default=0)
    episode_status = models.BooleanField(null=False, blank=True, default=False)
    episode_releaseDate = models.DateField(null=True, blank=True)
    episode_description = models.CharField(null=True, blank=True, max_length=4096)
    episode_viewcount = models.IntegerField(null=False, blank=True, default=0)
    episode_coverImage = models.ImageField(null=False, blank=True, upload_to=Episode_Cover_Images, validators=[validators.validate_image_extension], max_length=4092)
    episode_audioFile = models.FileField(null=False, blank=True, upload_to=Episode_Files, validators=[validators.validate_episode_extension])
    episode_price = models.IntegerField(null=False, blank=True, default=5)
    host = models.ForeignKey(HostsModel,related_name="episode_host", null=False, blank=True, default=1, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(CategoriesModel, related_name="episode_category", null=False, blank=True, default=1, on_delete=models.DO_NOTHING)
    podcast = models.ForeignKey(PodcastsModel, related_name="episode_podcast", null=False, blank=True, default=1, on_delete=models.DO_NOTHING)
    season = models.ForeignKey(SeasonsModel, related_name="episode_season",null=False, blank=True, default=1, on_delete=models.DO_NOTHING)
    encoder_FUI = models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        image = Image.open(self.episode_coverImage)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.episode_coverImage))
        self.episode_coverImage = compressed_image
        super(EpisodesModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}: {self.episode_name}"

# class PlayListsModel(models.Model):

#     class Meta:
#         ordering = ['id']

#     playlist_name = models.CharField(null=False, blank=True, max_length=256)
#     user_FUI = models.CharField(null=False, blank=True, max_length=1023)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at =models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.pk}: {self.playlist_name}"

# class PlayListEpisodesModel(models.Model):

#     class Meta:
#         ordering = ['id']

#     playlist_id = models.ForeignKey(PlayListsModel, null=False, blank=True, on_delete=models.CASCADE)
#     episode_id = models.ForeignKey(EpisodesModel, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.pk}: {self.playlist_id}"

# class FavouritesModel(models.Model):

#     class Meta:
#         ordering = ['id']

#     episode_id = models.ForeignKey(EpisodesModel, null=False, blank=True, on_delete=models.CASCADE)
#     user_FUI = models.CharField(null=False, blank=True, max_length=1023)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at =models.DateTimeField(auto_now=True)

# class PurchasedEpisodesModel(models.Model):

#     class Meta:
#         ordering = ['id']

#     episode_id = models.IntegerField(null=False, blank=True)
#     user_FUI = models.CharField(null=False, blank=True, max_length=1023)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at =models.DateTimeField(auto_now=True)

# class PurchasedSeasonsModel(models.Model):

#     class Meta:
#         ordering = ['id']

#     season_id = models.IntegerField(null=False, blank=True)
#     user_FUI = models.CharField(null=False, blank=True, max_length=1023)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at =models.DateTimeField(auto_now=True)