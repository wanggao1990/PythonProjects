
import xml.etree.ElementTree as ET
import os
from os import listdir, getcwd
from os.path import join

in_file ="01582.xml"
tree = ET.parse(in_file)
root = tree.getroot()

print(root.tag, "----", root.attrib)
#遍历root的下一层
for child in root:
    print("遍历root的下一层", child.tag, "----", child.attrib)

print(root[0].text)
print(root[1].text)



