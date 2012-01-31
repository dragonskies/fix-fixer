import xml.etree.ElementTree
import os

fix_xml = xml.etree.ElementTree.parse("fields.xml")

def find_tag_desc(find_tag):
    for each_element in fix_xml.getroot().getchildren():
        tag_text=each_element.find('.//Tag')
        #print tag_text.text
        desc_text = each_element.find('.//Desc')
        # print desc_text.text
        if tag_text.text == find_tag:
            return str(desc_text.text)
    #nothing found
    return "Not found"
