from os import listdir
from .src.parse_structure import parse_structure
from .src.parse_inline import parse_inline

def parse(md_path, html_path):
    '''
    Parses md file and outputs matching html file

    Args:
        md_path (str): Path to folder storing md files
        html_path (str): Path to folder for output html files

    Output:
        html files saved at html_path
    '''
    for file in listdir(md_path):
        file_path = md_path + '/' + file
        print(parse_inline(parse_structure(file_path)))
    