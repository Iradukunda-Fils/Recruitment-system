from django.apps import AppConfig


class JobPostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job_posts'
    def ready(self):
        import job_posts.signals
