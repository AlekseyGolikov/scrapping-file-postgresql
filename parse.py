import bs4

def get_items_list(items):
    
    for item in items:

        author = item.find('span', class_='author_list').text
        title = item.find('span', class_='title_list').text
        year = item.find('span', class_='book_year').text

        yield author, title, year

def get_links_list(links):

    for link in links:

        yield [link.get('href')]


def InsertBooksList():

    with open('text') as file:

        soup = bs4.BeautifulSoup(file.read(),'lxml')

        items = soup.find_all('div', class_='item_list')
        links = soup.find('div', class_='booklist').find_all('a')

        item = get_items_list(items)
        link = get_links_list(links)

        try:
            while item and link:
                row = []
                row.append(next(item))
                row.append(next(link))
                break
        except Exception as ex:
            pass
        finally:
            print(f'{row[0][0]} | {row[0][1]} | {row[0][2]} | {row[1][0]}')
            print(f'{type(row[0][0])} | {type(row[0][1])} | {type(row[0][2])} | {type(row[1][0])}')


if __name__ == "__main__":
    InsertBooksList()