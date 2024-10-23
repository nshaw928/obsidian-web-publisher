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
                    link_address = link_address.replace('%20', '-').replace(',', '').lower()

                    # Deal with internal Obsidian links
                    if len(link_address.split('.md')) == 2:
                        link_address = '/' + link_address.split('.')[0] + '.html'

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