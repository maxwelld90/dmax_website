from django.db import models

class Publication(models.Model):
    PUBLICATION_TYPE_FULLPAPER = 'FP'
    PUBLICATION_TYPE_SHORTPAPER = 'SP'
    PUBLICATION_TYPE_DEMO = 'D'
    PUBLICATION_TYPE_DOCCON = 'DC'
    PUBLICATION_TYPE_BOOK = 'B'
    PUBLICATION_TYPE_JOURNAL = 'J'
    PUBLICATION_TYPE_THESIS = 'T'
    
    PUBLICATION_TYPE_CHOICES = (
        (PUBLICATION_TYPE_FULLPAPER, 'Full Paper'),
        (PUBLICATION_TYPE_SHORTPAPER, 'Short Paper'),
        (PUBLICATION_TYPE_DEMO, 'Demo'),
        (PUBLICATION_TYPE_DOCCON, 'Doctoral Consortium'),
        (PUBLICATION_TYPE_BOOK, 'Book'),
        (PUBLICATION_TYPE_JOURNAL, 'Journal Article'),
        (PUBLICATION_TYPE_THESIS, 'Thesis'),
    )
    
    # Basic information
    
    title = models.TextField(blank=False,
                             max_length=200,
                             verbose_name='Publication Title',
                             help_text="Provide a title of the publication.")
    
    authors = models.TextField(blank=False,
                               max_length=200,
                               verbose_name='Author(s)',
                               help_text="Provide a list of author(s), each author separated by a comma and space.")
    
    published_date = models.DateField(blank=False,
                                      verbose_name='Publication Date',
                                      help_text="Select the date that the publication was issued.")
    
    doi = models.CharField(blank=True,
                           max_length=50,
                           verbose_name='DOI',
                           help_text="If the document has a DOI, enter this here. This can be left blank.")
    
    publication_type = models.CharField(blank=False,
                                        verbose_name='Publication Type',
                                        max_length=2,
                                        choices=PUBLICATION_TYPE_CHOICES,
                                        default=PUBLICATION_TYPE_FULLPAPER,
                                        help_text="Select the publication's type.")
    
    # Tagline (for the publications list) and abstract (full page view)
    
    tagline = models.TextField(blank=True,
                               verbose_name='Tagline text',
                               help_text="Text for the bottom of the publication grid box (i.e. Appeared in...) - HTML friendly.")
    
    abstract = models.TextField(blank=True,
                                verbose_name='Abstract text',
                                help_text="Add in an abstract for the publication. HTML friendly.")
    
    # Slug/URL information
    
    slug = models.SlugField(blank=True,
                            verbose_name='Publication slug',
                            help_text="Enter the slug for the publication URL. Spaces are dashes! If no URL or slug is supplied, no link is present. If no URL exists and a slug exists, an internal link is created.")
    
    external_url = models.URLField(blank=True,
                                   verbose_name='URL to external resource',
                                   help_text="Enter a URL to an external resource to link to. This takes precedent over an internal page; if a URL is supplied, this will be honoured first.")
    
    # Background image
    
    background = models.FileField(blank=True,
                                  upload_to='publications/backgrounds/',
                                  verbose_name='Background image',
                                  help_text="Select a JPG background image, typically 1500x500px.")
    
    ####################
    # Helper functions #
    ####################
    
    def publication_year(self):
        """
        Returns the year of publication from the publication date.
        """
        return self.published_date.strftime('%Y')
    
    def get_verbose_type(self):
        """
        Returns the verbose type for the publication.
        """
        return dict(self.PUBLICATION_TYPE_CHOICES)[self.publication_type]
    
    def get_authors_list(self):
        """
        Returns a list of authors - splitting at a ', '.
        """
        return self.authors.split(', ')


class PublicationResource(models.Model):
    pass