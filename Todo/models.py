from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Task:" + self.task + " Created:" + str(self.created_at)