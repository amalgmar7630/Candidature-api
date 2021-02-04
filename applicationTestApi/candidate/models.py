from django.utils.translation import ugettext_lazy as _

from django.db import models


class Candidate(models.Model):
    firstname = models.CharField(_('First Name'), max_length=30, db_index=True)
    lastname = models.CharField(_('Last Name'), max_length=30, db_index=True)
    email = models.CharField(_('Email'), max_length=200, db_index=True)
    birthdate = models.DateField(_("Birth Date"), null=True, db_index=True)
    phone = models.CharField(_("Phone Number"), max_length=8, null=True, unique=True, db_index=True)
    availability = models.PositiveIntegerField(_("Availability"), null=True, db_index=True)
    years_experience = models.PositiveIntegerField(_("Number Years Of Experience"), null=True, db_index=True)
    cv_file = models.FileField(_("Cv File"), upload_to="attachments/")
    message = models.TextField(_("Message"), null=True, blank=True, db_index=True)
    NEW = 'New'
    CONFIRMED = 'Confirmed'
    REJECTED = 'Rejected'
    APPLICATION_STATUS_CHOICES = [
        (NEW, 'New'),
        (CONFIRMED, 'Confirmed'),
        (REJECTED, 'Rejected'),
    ]
    application_status = models.CharField(
        max_length=30,
        choices=APPLICATION_STATUS_CHOICES,
        default=NEW,
    )

