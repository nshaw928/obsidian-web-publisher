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
            img_file = './assets/' + ''.join(img[img.index('(')+1:img.index(')')])
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