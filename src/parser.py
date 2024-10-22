from os import listdir
from .parse_functions.parse_structure import parse_structure
from .parse_functions.parse_inline import parse_inline

def parse(md_path):
    '''
    Parses directory of md file and outputs list of parsed html body content to be added to an html template.

    Args:
        md_path (str): Path to folder storing md files

    Output:
        website (list): Each element is a page on the website. Within each page, each element is a line. The name of the page is the last element in the page list.
    '''
    website = []

    for file in listdir(md_path):
        
        file_path = md_path + '/' + file
        website_page_content_list = parse_inline(parse_structure(file_path))

        file_name = file.split('.')[0]
        website_page_content_list.append(file_name)

        website.append(website_page_content_list)

    print(website)
    return website