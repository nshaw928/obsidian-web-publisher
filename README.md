# obsidian-web-publisher
## Running the program
To run the project, clone the directory, and edit the config.py file to add your website file paths. While in the directory, run publish.py to publish your site to the web (last part still under development).
```
git clone https://github.com/nshaw928/obsidian-web-publisher
cd path/to/wherever/you/cloned/this/project
python3 publish.py
```
### So what *can* it do right now?
Currently, the app will convert a folder of markdown files into a folder of html files. You can easily add these files to your GH Pages website if desired. Rest assured, future updates are coming soon to fully automate this process!

## Markdown Element Support
**Currently Supported Structural Markdown Elements**
- Headings 1-6
- Images
- Plain text
- Code

**Supported Inline Markdown Elements**
- Links, internal and external
- Italics (*)
- Bold (**)
- Bold Italics (***)

**Future Planned Elements to support**
- Quotes
- Unordered Lists
- Ordered Lists

## Future Plans
- Fully automate committing and pushing to Github
- Update README to include better instructions for use
- Clean setup.py and add more options
- Write tests