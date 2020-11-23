from django.db import models

class Ancestor(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_document = models.FileField(upload_to='ancestor_files')
    # death_date = models.DateField()
    # death_document = models.FileField()
    # marriage_date_1 = models.DateField()
    # marriage_document_1 = models.FileField()
    # marriage_date_2 = models.DateField()
    # marriage_document_2 = models.FileField()
    # marriage_date_3 = models.DateField()
    # marriage_document_3 = models.FileField()
    # additional_document_1 = models.FileField()
    # additional_document_2 = models.FileField()
    # additional_document_3 = models.FileField()
    notes = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
