# import datetime
# from django.core.exceptions import ValidationError
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import m2m_changed, pre_save
# from django.dispatch import receiver
# from django.template.loader import render_to_string
#
# from email import message
# from django.conf import settings
# from .models import Category, PostCategory, Post
#
#
# # Отправка сообщений
# def send_notifications(preview, pk, title, subscribers):
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=title, # Заголовок
#         body='', # Тело пустое т.к. используем шаблон
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers, # Кому отправляем
#     )
#     # Добавляем к сообщению наш шаблон
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.categories.all()
#         subscribers_emails = []
#
#         for cat in categories:
#             subscribers = cat.subscribers.all()
#             subscribers_emails += [a.email for a in subscribers] # Добавление почт подписчиков
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)
#
#
# # @receiver(pre_save, sender=Post)
# # def post_limit(sender, instance, **kwargs):
# #     today = datetime.date.today()
# #     post_limit = Post.objects.filter(author=instance.author, date_published__date=today).count()
# #     if post_limit >= 3:
# #         raise ValidationError('Нельзя публиковать бльше трех постов в сутки!!!')
#
