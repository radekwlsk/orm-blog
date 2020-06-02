from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BlogPost(models.Model):
    created = models.DateTimeField(_("created at"), auto_now_add=True)
    posted = models.DateTimeField(_("posted at"), null=True, blank=True)

    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(_("title"), max_length=256)
    body = models.TextField(_("body"))
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, related_name="+", null=True
    )

    sponsored = models.BooleanField(_("sponsored"), default=False)
    views = models.PositiveIntegerField(_("views"), default=0)
    thumbs_up = models.PositiveIntegerField(_("thumbs up"), default=0)
    thumbs_down = models.PositiveIntegerField(_("thumbs down"), default=0)


class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    website = models.URLField(_("website"), blank=True)


class Category(models.Model):
    name = models.CharField(max_length=128)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(_("comment text"), max_length=2000)
    post = models.ForeignKey(
        "BlogPost", on_delete=models.CASCADE, related_name="comments"
    )
