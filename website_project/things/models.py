from django.db import models

class Thing(models.Model):
    """
    A representation of a thing.
    """
    THING_URL_NONE = 'NO'
    THING_URL_INTERNAL = 'INT'
    THING_URL_EXTERNAL = 'EXT'
    
    THING_URL_TYPES = (
        (THING_URL_NONE, 'No URL'),
        (THING_URL_INTERNAL, 'Internal URL (uses slug)'),
        (THING_URL_EXTERNAL, 'External URL (opens new tab)'),
    )
    
    slug = models.SlugField(blank=True,
                            unique=True,
                            verbose_name='Thing slug',
                            help_text="Enter the slug for this instance. No spaces!")
    
    display_order = models.IntegerField(blank=False,
                                        verbose_name='Display order',
                                        default='1',
                                        help_text='Enter an integer that dictates the display order. Smaller is higher up the order.')
    
    span_width = models.IntegerField(blank=False,
                                     verbose_name='Column span',
                                     default='1',
                                     help_text='Enter an integer that determines how many columns the thing covers.')
    
    header = models.TextField(blank=False,
                              max_length=200,
                              verbose_name='Thing Title',
                              help_text="Provide a title for the thing.")
    
    blurb = models.TextField(blank=True,
                             verbose_name='Blurb',
                             help_text="Enter some descriptive blurb. HTML formatting is supported. Don't add a hyperlink.")
    
    background_blurb = models.BooleanField(blank=True,
                                           default=False,
                                           verbose_name='Apply background to blurb text?',
                                           help_text="Determines whether a background is applied to the text for the blurb. Can be used if background images are busy.")
    
    url_type = models.CharField(blank=False,
                                verbose_name='URL Type',
                                max_length=3,
                                choices=THING_URL_TYPES,
                                default=THING_URL_INTERNAL,
                                help_text="What type of URL (if any) for this thing?")
    
    external_url = models.URLField(blank=True,
                                   verbose_name='URL to external resource',
                                   help_text="Enter an external URL for this thing. Note that this only applies if the URL type is set to external.")
    
    background = models.FileField(blank=True,
                                  upload_to='things/grid-backgrounds/',
                                  verbose_name='Background grid image',
                                  help_text="Select an image for the thing's background.")
    
    background_colour = models.CharField(blank=False,
                                         verbose_name='Background colour',
                                         max_length=7,
                                         default='#0072C6',
                                         help_text="Enter a hex colour (including the hash) for the background colour of this thing.")
    
    text_colour = models.CharField(blank=False,
                                   verbose_name='Text colour',
                                   max_length=7,
                                   default='#FFFFFF',
                                   help_text="Enter a hex colour (including the hash) for the text colour of this thing.")
    
    darken_title_background_by = models.IntegerField(blank=False,
                                                     verbose_name='Darken title background colour (percentage)',
                                                     default='20',
                                                     help_text='Enter a value between 0 and 100 to darken the background colour of the header text by this percentage.')
    
    tags = models.TextField(blank=True,
                            verbose_name='Tag markup',
                            help_text="Enter markup for tags.")
    
    def __str__(self):
        return self.header