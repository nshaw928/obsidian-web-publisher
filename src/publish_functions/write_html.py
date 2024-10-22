def write_html(website_content, website_path):
    '''
    Creates html files and saves them inside the pages dir in website_path.

    Args:
        website_content (list): output of parse() function, containing website data.
        website_path (str): path to the repository where the website is stored locally.
    Output:
        website_content is saved in html files in website_path/pages/
    '''

    header_content = open('src/header_content.html')
    print(header_content.readlines())

    for i in range(len(website_content)):
        # Get page title
        title = website_content[i][-1]
        file_name = title.lower().replace(' ', '-').replace(',', '') + '.html'


        file = open(website_path + '/pages/' + file_name, 'w')
        html_template = [['<!DOCTYPE html>\n', '<html>\n', '<header>\n'], # 0
                         ['</header>\n', '<body>\n'], # 1
                         ['</body>\n', '</html>\n']] # 2
        
        # Write html template and header
        file.writelines(html_template[0])
        file.writelines(header_content)
        file.writelines(html_template[1])

        # Body and end of template
        body_content = website_content[i][:-1]
        for j in range(len(body_content)):
            file.write(body_content[j])
            file.write('\n')
        file.writelines(html_template[2])
        
        file.close()
        print(file_name + ' has been written')