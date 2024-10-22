from setup import load_config
from src.parser import parse
from src.publisher import publish

md_path, website_path = load_config()

# Parse MD and return HTML content
website_content = parse(md_path)

# Creates HTML files and (future) pushes to GitHub
publish(website_content, website_path)