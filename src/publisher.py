from .publish_functions.write_html import write_html
from .publish_functions.move_images import move_images

def publish(website_content, website_path, asset_path):
    
    write_html(website_content, website_path)

    move_images(asset_path, website_path)
    
    def push_to_github():
        '''
        
        '''