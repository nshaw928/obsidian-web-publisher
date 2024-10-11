from os import listdir

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
        parse_inline(parse_structure(file_path))

    def parse_structure(file_path):
        '''
        Parses a md file and outputs list containing parent html elements

        Args:
            file_path (str): file path of md file

        Output:
            page_structure (list): list of lists with each list containing 1 line [['<h1>', 'Title', '</h1>'], ['<p>', 'some text', '</p>']]
        '''
        page_structure = []

        # Open file and save contents as content
        with open(file_path, 'r') as file:
            content = file.read()

        code_start = False
        lines = content.split('\n')
        for line in lines:
            # Headers
            # TODO can consolidate the headers by using variable for number of # and f strings
            if line.startswith('#'):
                if line.startswith('# '):
                    h1 = [char for char in line]
                    page_structure.append(['<h1>', ''.join(h1[2:]), '</h1>'])
                if line.startswith('## '):
                    h2 = [char for char in line]
                    page_structure.append(['<h2>', ''.join(h2[3:]), '</h2>'])
                if line.startswith('### '):
                    h3 = [char for char in line]
                    page_structure.append(['<h3>', ''.join(h3[4:]), '</h3>'])
                if line.startswith('#### '):
                    h4 = [char for char in line]
                    page_structure.append(['<h4>', ''.join(h4[5:]), '</h4>'])
                if line.startswith('##### '):
                    h5 = [char for char in line]
                    page_structure.append(['<h5>', ''.join(h5[6:]), '</h5>'])
                if line.startswith('###### '):
                    h6 = [char for char in line]
                    page_structure.append(['<h6>', ''.join(h6[7:]), '</h6>'])

            # Images
            elif line.startswith('!['):
                img = [char for char in line]
                img_file = '/assets/' + ''.join(img[img.index('(')+1:img.index(')')])
                img_alt = ''.join(img[img.index('[')+1:img.index(']')])
                page_structure.append('<img src="' + img_file + '" alt="' + img_alt + '">')

            # Code
            elif line.startswith('```'):
                if code_start == False:
                    code_start = True
                    code_block = ''
                else:
                    code_start = False
                    page_structure.append('<pre><code>' + code_block + '</code></pre>')
            elif code_start == True:
                code_block = code_block + line + '\n'

            # Break
            elif len(line) == 0 and code_start == False:
                page_structure.append('<br>')
            # Assume plain text
            else:
                page_structure.append(['<p>', ''.join(line), '</p>'])
    
        return page_structure
    
    def parse_inline(page):
        '''
        Parses a page_structure list from the parse structure function and outputs list containing the lines of the html body.
        This function deals with links and text decorations.

        Args:
            page_structure (list): output of parse_structure(file_path)

        Output:
            body_content (list): list with each element containing 1 line ['<h1>Title</h1>', '<p>some text</p>']
        '''
        body_content = []

        for line in page:
            if len(line) == 3:
                tag_content = line[1]

                # Bold
                temp = []
                bold_split = tag_content.split('**')
                if len(bold_split) != 1:
                    for i in range(len(bold_split) - 1):
                        if i == 0 or i % 2 == 0:
                            temp.append(bold_split[i] + '<b>')
                        else:
                            temp.append(bold_split[i] + '</b>')
                    temp.append(bold_split[len(bold_split)-1])
                    tag_content = ''.join(temp)

                # Italics
                temp = []
                italics_split = tag_content.split('*')
                if len(italics_split) != 1:
                    for i in range(len(italics_split) - 1):
                        if i == 0 or i % 2 == 0:
                            temp.append(italics_split[i] + '<i>')
                        else:
                            temp.append(italics_split[i] + '</i>')
                    temp.append(italics_split[len(italics_split)-1])
                    tag_content = ''.join(temp)

                # Bold-Italics
                temp = []
                boldital_split = tag_content.split('***')
                if len(boldital_split) != 1:
                    for i in range(len(boldital_split) - 1):
                        if i == 0 or i % 2 == 0:
                            temp.append(boldital_split[i] + '<i>')
                        else:
                            temp.append(boldital_split[i] + '</i>')
                    temp.append(boldital_split[len(boldital_split)-1])
                    tag_content = ''.join(temp)

                # Links
                temp = tag_content.split('](')
                if len(temp) != 1:
                    # Get lists of link + addresses
                    link_texts = []
                    link_addresses = []
                    link_split = tag_content.split('[')[1:]
                    for i in range(0, len(link_split)):
                        link_texts.append(link_split[i].split(']')[0])
                    link_split = tag_content.split('(')[1:]
                    for i in range(0, len(link_split)):
                        link_addresses.append(link_split[i].split(')')[0])

                    i = 0
                    while '[' in tag_content:

                        link_text = link_texts[i]
                        link_address = link_addresses[i]

                        # Deal with internal Obsidian links
                        if len(link_address.split('.md')) == 2:
                            link_address = '/pages/' + link_address.split('.')[0] + '.html'

                        # Wrap link with html tags
                        link = ['<a href="', link_address, '">', link_text, '</a>']
                        link = ''.join(link)

                        # Format link around other text
                        temp = ''.join(tag_content)
                        link_chars = [char for char in temp]
                        link_start = link_chars.index('[')
                        link_end = link_chars.index(')')
                        tag_content = str(str(temp[:link_start]) + str(link) + str(temp[link_end+1::]))
                        i += 1
                
                # Update content of tag to the processed content
                line[1] = tag_content
                line = ''.join(line)
            else:
                pass
            
            body_content.append(line)
        
        return body_content