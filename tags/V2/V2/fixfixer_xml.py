"""XML-related functions for Fix Fixer"""

import xml.etree.ElementTree
import os

fix_xml = xml.etree.ElementTree.parse( os.path.join('resources', 'fields.xml') )

def find_tag_desc(find_tag):
    for each_element in fix_xml.getroot().getchildren():
        tag_text=each_element.find('.//Tag')
        #print tag_text.text
        desc_text = each_element.find('.//Desc')
        # print desc_text.text
        if tag_text.text == find_tag:
            return str(desc_text.text)
    #nothing found
    return "Tag [%s] could not be found." % find_tag
