import requests
import re


class Link:
    url = ''
    links = ''

    def __init__(self):
        self.url = input('Введите url сайта для парсинга всех ссылок:\n')

    def getLink(self):
        self.url = requests.get(self.url).text
        self.links = re.findall(r'\w+:\/\/[\w.-]+(?::?\d{1,5})?[-\w.\/?=&%]*', self.url)
        print('\n Результат: ')

    def writing_to_a_file(self):
        list_of_links = open('result.txt', 'w')
        for element in self.links:
            list_of_links.write(element)
            list_of_links.write('\n')
        list_of_links.close()

    def output_a_file(self):
        file = open('result.txt')
        print(file.read())

link = Link()
link.getLink()
link.writing_to_a_file()
link.output_a_file()
