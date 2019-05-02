BACKGROUND_MAPPINGS = {
    'canberra': 'Canberra, ACT, Australia - September 2016',
    'clashnessie': 'Clashnessie Bay, Highland, Scotland - July 2014',
    'diagram': 'PhD Writeup Hell - August 2018',
    'heraklion': 'Heraklion, Crete, Greece - July 2014',
    'jeir': 'Jeir, NSW, Australia - December 2016',
    'lilybank': 'Lilybank Gardens, Glasgow, Scotland - May 2018',
    'sandwood': 'Sandwood Bay, Highland, Scotland - July 2014',
    'shinjuku': 'Shinjuku, Tokyo, Japan - August 2017',
    'whitelee': 'Whitelee Windfarm, East Renfrewshire, Scotland - April 2015',
}

def apply_background_to_context(context_dict, background):
    """
    Given a context dictionary, adds the background and background identifier to the dictionary.
    If a mapping does not exist, only the background is appended.
    """
    context_dict['background'] = background
    
    if background in BACKGROUND_MAPPINGS:
        context_dict['background_identifier'] = BACKGROUND_MAPPINGS[background]