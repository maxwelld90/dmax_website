from django.db import models
from datetime import date

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
    
    published_in = models.TextField(blank=True,
                               verbose_name='Published in...',
                               help_text="What publication was the publication in? This is HTML friendly.")
    
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
    
    def has_been_published(self):
        """
        Returns True iif the publication date is before or equal to the current date.
        Returns False iif the publication date is in the future.
        """
        current_date = date.today()
        
        if self.published_date > current_date:
            return False
        
        return True
    
    ##################################
    # Helper functions for resources #
    ##################################
    
    def has_resources(self):
        """
        Returns True if at least one resource is present.
        """
        resources = PublicationResource.objects.all().filter(publication=self)
        
        if len(resources) > 0:
            return True
        
        return False
    
    def get_pdf_resource(self):
        """
        Returns a PublicationResource PDF object for the publication.
        Returns None if no object is present.
        """
        pdf = PublicationResource.objects.all().get(publication=self, resource_type=PublicationResource.RESOURCE_TYPE_PDF)
        return pdf
    
    def get_bibtex_resource(self):
        """
        Returns a PublicationResource BibTeX object for the publication.
        Returns None if no object is present.
        """
        bibtex = PublicationResource.objects.all().get(publication=self, resource_type=PublicationResource.RESOURCE_TYPE_BIBTEX)
        return bibtex
    
    def get_slides_resource(self):
        """
        Returns a PublicationResource slides object for the publication.
        Returns None if no object is present.
        """
        slides = PublicationResource.objects.all().get(publication=self, resource_type=PublicationResource.RESOURCE_TYPE_SLIDES)
        return slides
    
    def get_url_resources(self):
        """
        Returns a list of PublicationResource URL objects for the publication.
        Returns an empty list if none are present.
        """
        urls = PublicationResource.objects.all().filter(publication=self, resource_type=PublicationResource.RESOURCE_TYPE_URL)
        return urls
    
    ########
    # Meta #
    ########
    def __str__(self):
        return '({0}) {1}'.format(self.publication_year(), self.title)
    
    class Meta:
        """
        Meta class for the admin interface.
        """
        ordering = ['-published_date']
        verbose_name = 'publication'
        verbose_name_plural = 'publications'


class PublicationResource(models.Model):
    RESOURCE_TYPE_BIBTEX = 'BIB'
    RESOURCE_TYPE_PDF = 'PDF'
    RESOURCE_TYPE_SLIDES = 'SLI'
    RESOURCE_TYPE_URL = 'URL'
    
    RESOURCE_TYPE_CHOICES = (
        (RESOURCE_TYPE_BIBTEX, 'BibTeX'),
        (RESOURCE_TYPE_PDF, 'PDF of publication'),
        (RESOURCE_TYPE_SLIDES, 'Slides'),
        (RESOURCE_TYPE_URL, 'Link to resource'),
    )
    
    publication = models.ForeignKey(Publication,
                                    verbose_name='Associated Publication',
                                    help_text='Which publication is the resource associated with?',
                                    on_delete=models.CASCADE)
    
    resource_type = models.CharField(blank=False,
                                     verbose_name='Resource Type',
                                     max_length=3,
                                     choices=RESOURCE_TYPE_CHOICES,
                                     default=RESOURCE_TYPE_PDF,
                                     help_text="What kind of resource? This affects what fields below are considered.")
    
    bibtex = models.TextField(blank=True,
                              verbose_name='BiBTeX Source',
                              help_text="Enter the BiBTeX code for this publication.")
    
    pdf = models.FileField(blank=True,
                           upload_to='publications/pdf/',
                           verbose_name='PDF of Publication',
                           help_text="Select a PDF file to upload for this publication.")
    
    slides = models.FileField(blank=True,
                              upload_to='publications/slides/',
                              verbose_name='Slides of Publication',
                              help_text="Select PDF slides for the publication. Make sure fonts are removed!")
    
    external_url = models.URLField(blank=True,
                              verbose_name='URL to external resource',
                              help_text="Enter a URL to an external resource.")
    
    url_text = models.CharField(blank=True,
                                max_length=200,
                                verbose_name='Hyperlink text',
                                help_text="Enter text for the hyperlink. Leave blank to display the URL.")
    
    ########
    # Meta #
    ########
    def __str__(self):
        return '({0}) {1}'.format(self.publication, self.resource_type)
    
    class Meta:
        """
        Meta class for the admin interface.
        """
        ordering = ['publication']
        verbose_name = 'resource'
        verbose_name_plural = 'resources'