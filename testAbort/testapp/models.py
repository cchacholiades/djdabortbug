from django.db import models
from .tasks import test_abort_job
from dramatiq_abort import abort

class TestModel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    task_id = models.CharField(max_length=50, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.task_id:
            abort(self.task_id)
        set_task_id = self.test_dramatiq_job()
        if set_task_id:
            self.task_id = set_task_id
        super(TestModel, self).save(*args, **kwargs)


    def test_dramatiq_job(self):
        result = test_abort_job.send_with_options(
            args=('some message',),
            delay=271000,
        )
        if result:
            return result.message_id
        return None

