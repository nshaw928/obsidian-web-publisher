import os
import shutil

def move_images(asset_path, website_path):
    '''
    Moves images from the markdown assets folder into the website folder.

    Args:
        md_path (str): The path to the folder in which the markdown files and assets folder are stored.
        website_path (str): path to the repository where the website is stored locally.
    Output:
        Images are copied from md_path/assets to website_path/img
    '''

    for file in os.listdir(asset_path):
        source_path = asset_path + '/' + file
        dest_path = website_path + '/assets/' + file

        shutil.copyfile(source_path, dest_path)
