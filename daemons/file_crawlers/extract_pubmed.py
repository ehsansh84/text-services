import xml.etree.ElementTree as ET
import os

__author__ = 'Ehsan'


# for child in root:
#     print(child.tag)

# print(root[0][1].text)


root_dir = 'pubmed_samples'
info = os.walk(root_dir)
files_list = []

for dir, dirs, files in info:
    files_list = files
    # print(files)
    break

for file in files_list:
    tree = ET.parse(root_dir + '/' + file)
    root = tree.getroot()
    data = root.findall('./Journal/Volume/Issue/Article/ArticleInfo/ArticleTitle')
    print(file + 50 * '=')
    for d in data:
        print(d.tag)
        print(d.text.encode("utf-8"))
        # print(d.data)


# print(dir_list)

# article = {}
# articles = []
#


# f = open('../../input/66_2014_Article_786.xml', 'r')
# print(f.read())