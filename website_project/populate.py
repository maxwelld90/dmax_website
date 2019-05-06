import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_project.settings')

import django
django.setup()

import json
import shutil

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
POPULATION_DATA_ROOT = os.path.join(SCRIPT_DIRECTORY, 'populate_data')
UPLOADS_DIRECTORY = os.path.abspath(os.path.join(SCRIPT_DIRECTORY, 'uploads'))

def get_json_list(root_directory):
    """
    From root_directory, returns a list of absolute filenames to JSON files within the directory.
    """
    return_list = []
    
    for filename in os.listdir(root_directory):
        if filename.endswith('.json'):
            return_list.append(os.path.join(root_directory, filename))
    
    return return_list


def add_publication(json_path):
    """
    Given an absolute path to a publication's JSON file, adds the publication to the database.
    """
    print(">> Adding publication '{0}'".format(json_path))
    json_root = os.path.dirname(os.path.realpath(json_path))
    
    with open(json_path, 'r') as f:
        json_data = json.load(f)
        
        new_publication = models.Publication()
        already_exists = does_publication_exist(json_data['publication']['slug'])
        
        if already_exists:
            print(">> Already exists, replacing!")
            new_publication = already_exists
        
        for (key, value) in json_data['publication'].items():
            
            if key == 'abstract':
                value = get_text_file(json_root, value)
            elif key == 'background':
                back_abs_path = os.path.abspath(os.path.join(json_root, value))
                back_filename = '{0}.jpg'.format(json_data['publication']['slug'])
                
                new_publication.background.save(back_filename, File(open(back_abs_path, 'rb')))
            
            if key != 'background':
                setattr(new_publication, key, value)
        
        new_publication.save()
        
        add_publication_resources(json_root, json_data, new_publication)


def add_publication_resources(json_root, json_data, new_publication):
    """
    Given the JSON data and Publication object, adds new PublicationResource objects where required.
    """
    # First, delete all instances of existing PublicationResource objects for the given publication.
    models.PublicationResource.objects.all().filter(publication=new_publication).delete()
    
    # Now, iterate through each resource. Create an object for each, linking to the Publication.
    for (key, value) in json_data['resources'].items():
        resource_object = models.PublicationResource()
        resource_object.publication = new_publication
        
        resource_object.resource_type = key
        
        if key == 'BIB':
            resource_object.bibtex = get_text_file(json_root, value)
        elif key == 'PDF':
            pdf_abs_path = os.path.abspath(os.path.join(json_root, value))
            pdf_filename = '{0}.pdf'.format(new_publication.slug)
            
            resource_object.pdf.save(pdf_filename, File(open(pdf_abs_path, 'rb')))
        elif key == 'SLI':
            sli_abs_path = os.path.abspath(os.path.join(json_root, value))
            sli_filename = '{0}.pdf'.format(new_publication.slug)
            
            resource_object.slides.save(sli_filename, File(open(sli_abs_path, 'rb')))
        elif key == 'URL':
            if 'url_text' in value:
                resource_object.url_text = value['url_text']
            
            resource_object.external_url = value['external_url']
            
        resource_object.save()
    


def get_text_file(json_root, relative_path):
    """
    Returns a string representation of the contents of the file specified by filename.
    """
    text_abs_path = os.path.abspath(os.path.join(json_root, relative_path))
    return_str = ""
    
    with open(text_abs_path, 'r') as f:
        return_str = f.read()
    
    return return_str


def does_publication_exist(slug):
    """
    Checks whether the publication already exists in the database.
    If so, the Publication object is returned. Otherwise, False is returned.
    """
    try:
        publication = models.Publication.objects.all().get(slug=slug)
    except models.Publication.DoesNotExist:
        return False
    
    return publication


def do_publications():
    """
    Populates the database with publications.
    """
    print(">  Adding publications...")
    json_directory = os.path.join(POPULATION_DATA_ROOT, 'publications', 'json')
    json_list = get_json_list(json_directory)
    
    for json_file in json_list:
        add_publication(json_file)


def tidy_uploads():
    """
    Tidies up the uploads directory before beginning the population process.
    Avoids issues with the same file appearing multiple times in the uploads directory.
    """
    shutil.rmtree(os.path.join(UPLOADS_DIRECTORY, 'publications'), ignore_errors=True)


def main():
    """
    Where the magic happens!
    """
    tidy_uploads()
    do_publications()
    

if __name__ == "__main__":
    print("Running dmax.org.uk population script...")
    
    from dmax_org_uk import models
    from django.core.files import File
    
    main()