# from django.core.management import BaseCommand
# from users.models import User
#
# from os import getenv
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         user = User.objects.create(
#             username='admin',
#             email=getenv('ADMIN_EMAIL'),
#             first_name='Admin',
#             last_name='Adminskiy',
#             is_staff=True,
#             is_superuser=True,
#             is_active=True
#         )
#
#         user.set_password(getenv('ADMIN_PASSWORD'))
#         user.save()