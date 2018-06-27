
import xml.etree.ElementTree as ET
import os
from os import listdir, getcwd

files_dir = "."
save_path = "yyy/zzz"

in_file ="01582.xml"

folder = save_path.split("/",1)[-1]

print(folder)

for rt, dirs, files in os.walk(files_dir):
    for f in files:

        f = in_file

        ext = os.path.splitext(f)[1]
        if ext == ".xml":

            tree = ET.parse(f)
            root = tree.getroot()


            root[0].text = folder
            root[2].text = os.path.abspath(os.path.join(save_path, in_file))

            tree.write("22601.xml",encoding="utf-8",xml_declaration=True)
