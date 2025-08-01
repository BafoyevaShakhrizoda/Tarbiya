from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.projects.utils import notify_subscribers
from apps.projects.models import Books, Banner, Videos, Music, TextBooks

@receiver(post_save, sender=Books)
def notify_book_created(sender, instance, created, **kwargs):
    if created:
        subject = f" Yangi kitob: {instance.title}"
        message = f"{instance.description or ''}\n\nYuklab olish: https://example.com/books/{instance.pk}"
        notify_subscribers(subject, message)

@receiver(post_save, sender=Banner)
def notify_banner_created(sender, instance, created, **kwargs):
    if created and instance.is_active:
        subject = f" Yangi banner: {instance.title}"
        message = f"{instance.description or ''}\n\nSahifaga o'tish: {instance.link or 'https://example.com'}"
        notify_subscribers(subject, message)

@receiver(post_save, sender=Videos)
def notify_videos_created(sender, instance, created, **kwargs):
    if created and instance.is_active:
        subject = f" Yangi video: {instance.title}"
        message = f"{instance.description or ''}\n\nVideoni ko'rish: {instance.video or 'https://example.com'}"
        notify_subscribers(subject, message)

@receiver(post_save, sender=TextBooks)
def notify_textbooks_created(sender, instance, created, **kwargs):
    if created and instance.is_active:
        subject = f"Yangi darslik: {instance.title}"
        message = f"{instance.description or ''}\n\nDarslikni ko‘rish: {instance.link or 'https://example.com'}"
        notify_subscribers(subject, message)

@receiver(post_save, sender=Music)
def notify_audio_created(sender, instance, created, **kwargs):
    if created and instance.is_active:
        subject = f"Yangi audio: {instance.title}"
        message = f"{instance.description or ''}\n\nAudioni ko‘rish: {instance.link or 'https://example.com'}"
        notify_subscribers(subject, message)
