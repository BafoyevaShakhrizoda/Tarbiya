from django.core.mail import send_mail
from .models import Subscription
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def notify_subscribers(subject, message):
    emails = list(Subscription.objects.values_list('email', flat=True))

    if not emails:
        logger.info("Jo'natish uchun email yo'q.")
        return

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=emails,
            fail_silently=False
        )
        logger.info(f"Habar {len(emails)} kuzatuvchiga yuborildi.")
    except Exception as e:
        logger.error(f"Jo'natishda hatolik boldi: {e}")
