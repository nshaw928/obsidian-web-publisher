from os import listdir
from parse_functions.parse_structure import parse_structure
from parse_functions.parse_inline import parse_inline

def parse(md_path):
    '''
    Parses md file and outputs matching html file

    Args:
        md_path (str): Path to folder storing md files

    Output:
        website_page_content_list (list): A list where each element is a list containing each line of the webpage body as an element.
    '''
    for file in listdir(md_path):
        file_path = md_path + '/' + file
        print(file)
        print(parse_inline(parse_structure(file_path)))