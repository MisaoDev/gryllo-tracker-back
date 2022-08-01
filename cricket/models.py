from tabnanny import verbose
from django.db import models
from django.forms import CharField
from django.utils.translation import gettext_lazy as _


class Cricket(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    class WingLength(models.TextChoices):
        GREATER_THAN = 'GT', _('Longer than forewings')
        EQUAL = 'EQ', _('Same as forewings')
        LEST_THAN = 'LT', _('Shorter than forewings')

    name = models.CharField(
        _('name'),
        max_length=30,
    )

    sex = models.CharField(
        _('sex'),
        max_length=1,
        choices=Sex.choices,
    )

    date_of_birth = models.DateField(
        _('date of birth'),
        blank=True,
        null=True,
    )

    is_adult = models.BooleanField(
        _('is adult'),
        blank=True,
        null=True,
    )

    wing_length = models.CharField(
        _('hindwing length'),
        max_length=2,
        choices=WingLength.choices,
        blank=True,
    )

    antenna_length = models.IntegerField(
        _('antenna length'),
        help_text=_('Antenna length in milimeters'),
        blank=True,
        null=True,
    )

    location = models.ForeignKey(
        'Terrarium',
        verbose_name=_('location'),
        related_name='crickets',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('cricket')
        verbose_name_plural = _('crickets')


class CricketEvent(models.Model):
    class EventType(models.TextChoices):
        BIRTH = 'BIRTH', _('Birth')
        DEATH = 'DEATH', _('Death')
        MOLT = 'MOLT', _('Molt')
        OTHER = 'OTHER', _('Other')

    name = models.CharField(
        _('name'),
        max_length=30,
    )

    cricket = models.ForeignKey(
        'Cricket',
        verbose_name=_('cricket'),
        related_name='events',
        on_delete=models.CASCADE,
    )

    type = models.CharField(
        _('event type'),
        max_length=5,
        choices=EventType.choices,
    )

    event_date = models.DateField(
        _('event date'),
        blank=True,
        null=True,
    )

    event_time = models.TimeField(
        _('event time'),
        blank=True,
        null=True,
    )

    notes = models.TextField(
        _('notes'),
        max_length=2000,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('cricket event')
        verbose_name_plural = _('cricket events')


class CricketMolt(models.Model):
    event = models.OneToOneField(
        'CricketEvent',
        verbose_name=_('cricket molt'),
        related_name='molt',
        on_delete=models.CASCADE,
    )

    becomes_adult = models.BooleanField(
        _('becomes adult'),
        blank=True,
        null=True,
    )

    grows_wings = models.BooleanField(
        _('grows wings'),
        blank=True,
        null=True,
    )

    grows_ovopositor = models.BooleanField(
        _('grows ovopositor'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.event.cricket} - {self.event.event_date}'

    class Meta:
        verbose_name = _('cricket molt')
        verbose_name_plural = _('cricket molts')


class Terrarium(models.Model):
    name = models.CharField(
        _('name'),
        max_length=30,
    )

    description = models.TextField(
        _('description'),
        max_length=2000,
        blank=True,
    )

    accessories = models.ManyToManyField(
        'Accessory',
        verbose_name=_('accessories'),
        related_name='terrariums',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('terrarium')
        verbose_name_plural = _('terrariums')


class Accessory(models.Model):
    name = models.CharField(
        _('name'),
        max_length=30,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('terrarium accessory')
        verbose_name_plural = _('terrarium accessories')
