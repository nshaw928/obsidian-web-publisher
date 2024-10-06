# obsidian-web-publisher
## Program Structure
### Running the program
To run the program, place the project folder in the obsidian vault. Edit the config.py file to add your website file paths. While in the directory, run publish.py to publish your site.
```
cd path/to/your/website/vault
python3 publish.py
```
**Project Folder Structure**
- publish.py
    - publish()
- config.py
- README.md
- LICENSE
- .gitignore
- src/
    - setup.py
        - load_config()
    - parser.py
        - parse_structure()
        - parse_inline()
        - output_html()
    - publisher (BASH OR .PY?)
- tests/
    - test.md
    - parser_tests.py
        - parse_structure_test()
        - parse_inline_test()
        - output_html_test()