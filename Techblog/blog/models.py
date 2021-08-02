from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django_editorjs_fields import EditorJsJSONField, EditorJsTextField

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    ContactNo= models.PositiveBigIntegerField()
    Message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    full_name = models.CharField(max_length=100, help_text='Help people discover your account by using the name',null=True)
    email = models.EmailField(unique=True)
    # last_name=None
    # first_name=None

    # Optional fields
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10,null=True, blank=True)
    
    def str(self):
        return self.username
class Post(models.Model):
    body_default = models.TextField()
    body_editorjs = EditorJsJSONField(readOnly=False, autofocus=True)
    body_custom = EditorJsJSONField(
        plugins=[
            "@editorjs/image",
            "@editorjs/header",
            "@editorjs/list",
            "editorjs-github-gist-plugin",
            "editorjs-hyperlink",
            "@editorjs/code",
            "@editorjs/inline-code",
            "@editorjs/table@1.3.0",
        ],
        tools={
            "Gist": {
                "class": "Gist"
            },
            "Hyperlink": {
                "class": "Hyperlink",
                "config": {
                    "shortcut": 'CMD+L',
                    "target": '_blank',
                    "rel": 'nofollow',
                    "availableTargets": ['_blank', '_self'],
                    "availableRels": ['author', 'noreferrer'],
                    "validate": False,
                }
            },
            "Image": {
                'class': 'ImageTool',
                "config": {
                    "endpoints": {
                        # Your custom backend file uploader endpoint
                        "byFile": "/editorjs/image_upload/"
                    }
                }
            }
        },
        null=True,
        blank=True,
    )
    body_textfield = EditorJsTextField(  # only images and paragraph (default)
        plugins=["@editorjs/image"], null=True, blank=True,
        i18n={
            'messages': {
                'blockTunes': {
                    "delete": {
                        "Delete": "Удалить"
                    },
                    "moveUp": {
                        "Move up": "Переместить вверх"
                    },
                    "moveDown": {
                        "Move down": "Переместить вниз"
                    }
                }
            },
        }
    )

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.id})

    def __str__(self):
        return '{}'.format(self.id)