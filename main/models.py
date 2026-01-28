from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Service(TimestampedModel):
    title_ru = models.CharField(max_length=200)
    title_kk = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_kk = models.TextField()
    description_en = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title_ru"]

    def __str__(self):
        return self.title_ru


class TrainingProgram(TimestampedModel):
    title_ru = models.CharField(max_length=200)
    title_kk = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_kk = models.TextField()
    description_en = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title_ru"]

    def __str__(self):
        return self.title_ru


class LegalDocument(TimestampedModel):
    title_ru = models.CharField(max_length=220)
    title_kk = models.CharField(max_length=220)
    title_en = models.CharField(max_length=220)
    link_url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title_ru"]

    def __str__(self):
        return self.title_ru


class NewsItem(TimestampedModel):
    title_ru = models.CharField(max_length=220)
    title_kk = models.CharField(max_length=220)
    title_en = models.CharField(max_length=220)
    summary_ru = models.TextField()
    summary_kk = models.TextField()
    summary_en = models.TextField()
    published_at = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title_ru


class Proposal(TimestampedModel):
    title_ru = models.CharField(max_length=200)
    title_kk = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_kk = models.TextField()
    description_en = models.TextField()

    def __str__(self):
        return self.title_ru


class StructureUnit(TimestampedModel):
    title_ru = models.CharField(max_length=200)
    title_kk = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_kk = models.TextField()
    description_en = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title_ru"]

    def __str__(self):
        return self.title_ru


class Branch(TimestampedModel):
    name_ru = models.CharField(max_length=200)
    name_kk = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    location_ru = models.CharField(max_length=200)
    location_kk = models.CharField(max_length=200)
    location_en = models.CharField(max_length=200)
    description_ru = models.TextField()
    description_kk = models.TextField()
    description_en = models.TextField()

    def __str__(self):
        return self.name_ru


class FeedbackMessage(TimestampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"
