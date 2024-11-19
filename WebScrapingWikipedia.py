import requests
from bs4 import BeautifulSoup

# URL of a Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table
    table = soup.find('table', class_='wikitable')

    if table:
        print("Table data with column titles:")
        
        # Extract column titles
        headers = table.find('tr').find_all('th')
        column_titles = [header.text.strip() for header in headers]
        print("Column titles:", column_titles)

        # Extract row data
        rows = table.find_all('tr')
        for row in rows[1:6]:  # Limit to 5 rows
            cells = row.find_all('td')
            data = [cell.text.strip() for cell in cells]
            print(data)
    else:
        print("Table not found")
else:
    print("Error retrieving the page")
