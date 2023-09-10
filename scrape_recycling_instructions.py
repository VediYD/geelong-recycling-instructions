# imports

# installed imports
from bs4 import BeautifulSoup
from pandas import DataFrame

# built in imports
from requests import get


# pulling the data from city of greater geelong website
url = "https://www.geelongaustralia.com.au/recycling/guide/default.aspx"
html = get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# getting the list of materials defined here
ul_element = soup.find('ul', {'class': 'nav nav-menu'})
li_elements = ul_element.find_all('li')

# stores where every type of material needs to go
material_bin = {
    'material': [],
    'sub_material': [],
    'instructions': [],
}
for li in li_elements:
    sub_url = url.replace('default.aspx', li.a['href'])
    material = li.a.text
    sub_html = get(sub_url)
    sub_soup = BeautifulSoup(sub_html.text, 'html.parser')
    sub_elements = sub_soup.findAll('div', {'class': "panel panel-expand"})
    for element in sub_elements:
        sub_material = element.find('div', {'class': 'panel-heading'}).a.text.strip().lower()
        instructions = element.find('div', {'class': 'panel-body'}).find('div', {'class': 'read-text'})
        instructions = instructions.text.strip().replace('\n', ' ').replace('\xa0', '').replace('\r', '')
        instructions = instructions.replace('What to do with it?', '').replace('Did you know?', '')

        # save information scrapped
        material_bin['material'].append(material)
        material_bin['sub_material'].append(sub_material)
        material_bin['instructions'].append(instructions)


data = DataFrame(material_bin)

# exporting the dataset and manually classify the bins to which they belong
data.to_csv('recycling_instructions.csv', index=False)