# import datetime
# import math
# from dateutil.relativedelta import relativedelta
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from core.models import SatisHesabat, CalculateTable



# @receiver(post_save, sender=SatisHesabat)
# def create_satis_hesabat(sender, instance, created, **kwargs):
#     if created:
#         today = datetime.date.today()
#         count = instance.month
#         month_period = 1
#         while count > 0:
#             CalculateTable.objects.create(
#                 satis_hesabat=instance,
#                 month = month_period,
#                 amount = instance.price / instance.month,
#                 pay_date = today + relativedelta(months=month_period)
#             )
#             count -= 1
#             month_period += 1
