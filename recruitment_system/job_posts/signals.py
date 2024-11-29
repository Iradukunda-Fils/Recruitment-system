from django.dispatch import  receiver
from django.db.models.signals import pre_save  
from job_posts.models import Job

# @receiver(pre_save, sender=Job, weak=True, dispatch_uid='Job_posting_pre_save')
# def set_the_data_pre_save(sender, instance, **kwargs):
#     if not instance.company:
        