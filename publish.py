from setup import load_config
from parser import parse
from publisher import publish

md_path, html_path = load_config()

parse(md_path, html_path)